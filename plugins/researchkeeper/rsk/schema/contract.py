"""Stable scientific schema roles, proposal parsing, and validation."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from types import MappingProxyType
from typing import Any, Mapping

import yaml


SCIENTIFIC_ROLES = frozenset(
    {
        "literature",
        "entities",
        "methods",
        "conditions",
        "results",
        "relations",
        "claims",
    }
)
VECTOR_GATE_LANGUAGES = frozenset({"zh", "en", "mixed"})
REQUIRED_VECTOR_GATE_SCENARIOS = frozenset(
    {
        "quantitative_range",
        "cross_module_multi_hop",
        "source_constraint",
        "negation",
        "ambiguous_topic",
        "conflict_evidence",
        "out_of_domain",
    }
)
_MODULE_FIELDS = (
    "name",
    "display",
    "file",
    "role",
    "description",
    "trigger_keywords",
    "extract_rules",
    "audit_focus",
)
_SAFE_NAME = re.compile(r"^[a-z][a-z0-9_-]*$")
_SAFE_FILE = re.compile(r"^[a-z][a-z0-9_-]*\.md$")
_DRIVE_PATH = re.compile(r"^[A-Za-z]:")


@dataclass(frozen=True)
class SchemaModule:
    name: str
    display: str
    file: str
    role: str
    description: str
    trigger_keywords: tuple[str, ...]
    extract_rules: Mapping[str, str]
    audit_focus: tuple[str, ...]

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "SchemaModule":
        extract_rules = value.get("extract_rules") or {}
        return cls(
            name=str(value.get("name", "")),
            display=str(value.get("display", "")),
            file=str(value.get("file", "")),
            role=str(value.get("role", "")),
            description=str(value.get("description", "")),
            trigger_keywords=tuple(
                str(item) for item in (value.get("trigger_keywords") or ())
            ),
            extract_rules=MappingProxyType(
                {str(key): str(item) for key, item in extract_rules.items()}
            ),
            audit_focus=tuple(
                str(item) for item in (value.get("audit_focus") or ())
            ),
        )

    def as_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "display": self.display,
            "file": self.file,
            "role": self.role,
            "description": self.description,
            "trigger_keywords": list(self.trigger_keywords),
            "extract_rules": dict(self.extract_rules),
            "audit_focus": list(self.audit_focus),
        }


@dataclass(frozen=True)
class SchemaProposal:
    template_id: str
    template_version: str
    schema_version: str
    modules: tuple[SchemaModule, ...]
    vector_gate_queries: tuple[Mapping[str, object], ...]
    vector_gate_chain_queries: tuple[Mapping[str, object], ...] = ()

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "SchemaProposal":
        return cls(
            template_id=str(value.get("template_id", "")),
            template_version=str(value.get("template_version", "")),
            schema_version=str(value.get("schema_version", "")),
            modules=tuple(
                SchemaModule.from_mapping(item)
                for item in (value.get("modules") or ())
            ),
            vector_gate_queries=tuple(
                MappingProxyType(dict(item))
                for item in (value.get("vector_gate_queries") or ())
            ),
            vector_gate_chain_queries=tuple(
                MappingProxyType(dict(item))
                for item in (value.get("vector_gate_chain_queries") or ())
            ),
        )

    def as_dict(self) -> dict[str, object]:
        return {
            "template_id": self.template_id,
            "template_version": self.template_version,
            "schema_version": self.schema_version,
            "modules": [module.as_dict() for module in self.modules],
            "vector_gate_queries": [
                dict(query) for query in self.vector_gate_queries
            ],
            "vector_gate_chain_queries": [
                dict(query) for query in self.vector_gate_chain_queries
            ],
        }


@dataclass(frozen=True)
class SchemaPaths:
    modules: Path
    vector_gate_queries: Path
    index: Path
    schema: Path
    reviewer: Path


def _read_mapping(path: Path) -> Mapping[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        value = json.loads(text)
    else:
        value = yaml.safe_load(text)
    if not isinstance(value, dict):
        raise ValueError(f"schema document must be an object: {path}")
    return value


def load_proposal(path: Path) -> SchemaProposal:
    return SchemaProposal.from_mapping(_read_mapping(path))


def builtin_template_root() -> Path:
    """Resolve immutable built-in assets from Claude plugin or installation."""
    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT")
    if plugin_root:
        return Path(plugin_root).resolve() / "schemas"
    source_root = Path(__file__).resolve().parents[2] / "schemas"
    if source_root.is_dir():
        return source_root
    return Path(sys.prefix).resolve() / "schemas"


def load_builtin_template(
    template_id: str,
    *,
    template_root: Path | None = None,
) -> SchemaProposal:
    root = (template_root or builtin_template_root()).resolve()
    template_dir = root / template_id
    modules_payload = _read_mapping(template_dir / "modules.yaml")
    gate_payload = _read_mapping(template_dir / "vector_gate_queries.yaml")
    payload = {
        "template_id": modules_payload.get("template_id", template_id),
        "template_version": modules_payload.get("template_version", "1"),
        "schema_version": modules_payload.get("schema_version", "schema_v1"),
        "modules": modules_payload.get("modules", ()),
        "vector_gate_queries": gate_payload.get("test_queries", ()),
        "vector_gate_chain_queries": gate_payload.get(
            "chain_test_queries",
            (),
        ),
    }
    proposal = SchemaProposal.from_mapping(payload)
    errors = [
        *validate_proposal(proposal),
        *validate_builtin_vector_gate(proposal),
    ]
    if errors:
        raise ValueError("; ".join(errors))
    return proposal


def _validate_safe_module(module: SchemaModule) -> list[str]:
    errors: list[str] = []
    if not _SAFE_NAME.fullmatch(module.name):
        errors.append(f"module name is not safe: {module.name!r}")
    if (
        not _SAFE_FILE.fullmatch(module.file)
        or _DRIVE_PATH.match(module.file)
        or "/" in module.file
        or "\\" in module.file
        or ".." in module.file
        or Path(module.file).is_absolute()
    ):
        errors.append(f"module file is not a safe relative filename: {module.file!r}")
    if module.role not in SCIENTIFIC_ROLES:
        errors.append(f"unknown role for {module.name!r}: {module.role!r}")
    if not module.display.strip():
        errors.append(f"module display is required: {module.name!r}")
    if not module.description.strip():
        errors.append(f"module description is required: {module.name!r}")
    if not module.trigger_keywords:
        errors.append(f"trigger_keywords are required: {module.name!r}")
    if not module.extract_rules:
        errors.append(f"extract_rules are required: {module.name!r}")
    if not module.audit_focus:
        errors.append(f"audit_focus is required: {module.name!r}")
    return errors


def _validate_vector_gate_query(
    query: Mapping[str, object],
    *,
    index: int,
) -> list[str]:
    errors: list[str] = []
    text = query.get("query")
    expected_role = query.get("expected_role")
    if not isinstance(text, str) or not text.strip():
        errors.append(f"vector gate query {index} requires query text")
    if (
        not isinstance(expected_role, str)
        or expected_role not in SCIENTIFIC_ROLES
    ):
        errors.append(
            f"vector gate query {index} has invalid expected_role: "
            f"{expected_role!r}"
        )
    return errors


def _validate_chain_query(
    query: Mapping[str, object],
    *,
    index: int,
) -> list[str]:
    errors: list[str] = []
    text = query.get("query")
    expected_roles = query.get("expected_roles")
    if not isinstance(text, str) or not text.strip():
        errors.append(f"vector gate chain query {index} requires query text")
    if (
        not isinstance(expected_roles, (list, tuple))
        or len(expected_roles) < 2
        or any(
            not isinstance(role, str) or role not in SCIENTIFIC_ROLES
            for role in expected_roles
        )
    ):
        errors.append(
            f"vector gate chain query {index} requires at least two "
            "valid expected_roles"
        )
    return errors


def validate_builtin_vector_gate(proposal: SchemaProposal) -> list[str]:
    """Validate the expanded public benchmark for a built-in template."""
    errors: list[str] = []
    if len(proposal.vector_gate_queries) < 20:
        errors.append("built-in vector gate requires at least 20 test queries")
    if len(proposal.vector_gate_chain_queries) < 10:
        errors.append(
            "built-in vector gate requires at least 10 chain test queries"
        )

    role_counts = {
        role: sum(
            query.get("expected_role") == role
            and query.get("expected_behavior") != "no_relevant_result"
            for query in proposal.vector_gate_queries
        )
        for role in SCIENTIFIC_ROLES
    }
    underrepresented = sorted(
        role for role, count in role_counts.items() if count < 2
    )
    if underrepresented:
        errors.append(
            "built-in vector gate roles require two ground-truth queries: "
            + ", ".join(underrepresented)
        )

    language_count = sum(
        query.get("language") in {"en", "mixed"}
        for query in proposal.vector_gate_queries
    )
    if language_count < 5:
        errors.append(
            "built-in vector gate requires at least five English or mixed "
            "queries"
        )

    benchmark_queries = (
        *proposal.vector_gate_queries,
        *proposal.vector_gate_chain_queries,
    )
    scenarios = {
        str(query.get("scenario"))
        for query in benchmark_queries
        if query.get("scenario")
    }
    missing_scenarios = sorted(REQUIRED_VECTOR_GATE_SCENARIOS - scenarios)
    if missing_scenarios:
        errors.append(
            "built-in vector gate scenarios missing: "
            + ", ".join(missing_scenarios)
        )

    for index, query in enumerate(benchmark_queries):
        language = query.get("language")
        scenario = query.get("scenario")
        if language not in VECTOR_GATE_LANGUAGES:
            errors.append(
                f"built-in vector gate query {index} has invalid language: "
                f"{language!r}"
            )
        if not isinstance(scenario, str) or not scenario.strip():
            errors.append(
                f"built-in vector gate query {index} requires scenario"
            )
    return errors


def validate_proposal(proposal: SchemaProposal) -> list[str]:
    errors: list[str] = []
    if not proposal.template_id.strip():
        errors.append("template_id is required")
    if not proposal.template_version.strip():
        errors.append("template_version is required")
    if proposal.schema_version != "schema_v1":
        errors.append("schema_version must be schema_v1")
    if not proposal.modules:
        errors.append("at least one module is required")

    names: set[str] = set()
    files: set[str] = set()
    roles: set[str] = set()
    literature_count = 0
    for module in proposal.modules:
        errors.extend(_validate_safe_module(module))
        if module.name in names:
            errors.append(f"duplicate module name: {module.name}")
        if module.file in files:
            errors.append(f"duplicate module file: {module.file}")
        names.add(module.name)
        files.add(module.file)
        roles.add(module.role)
        if module.role == "literature":
            literature_count += 1

    missing_roles = sorted(SCIENTIFIC_ROLES - roles)
    if missing_roles:
        errors.append(f"roles not represented: {', '.join(missing_roles)}")
    if literature_count != 1:
        errors.append("exactly one module must map to literature")

    if not proposal.vector_gate_queries:
        errors.append("at least one vector gate query is required")
    query_roles: set[object] = set()
    for index, query in enumerate(proposal.vector_gate_queries):
        errors.extend(_validate_vector_gate_query(query, index=index))
        expected_role = query.get("expected_role")
        if (
            isinstance(expected_role, str)
            and expected_role in SCIENTIFIC_ROLES
        ):
            query_roles.add(expected_role)
    missing_query_roles = sorted(SCIENTIFIC_ROLES - query_roles)
    if missing_query_roles:
        errors.append(
            "vector gate roles not represented: "
            + ", ".join(missing_query_roles)
        )
    for index, query in enumerate(proposal.vector_gate_chain_queries):
        errors.extend(_validate_chain_query(query, index=index))
    return errors


def schema_fingerprint(paths: SchemaPaths) -> str:
    digest = hashlib.sha256()
    for label, path in (
        ("modules", paths.modules),
        ("vector_gate_queries", paths.vector_gate_queries),
        ("index", paths.index),
        ("schema", paths.schema),
        ("reviewer", paths.reviewer),
    ):
        digest.update(label.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()
