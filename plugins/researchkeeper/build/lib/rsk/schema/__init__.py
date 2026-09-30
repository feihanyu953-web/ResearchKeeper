"""Scientific schema onboarding contracts."""

from .contract import (
    SCIENTIFIC_ROLES,
    SchemaModule,
    SchemaPaths,
    SchemaProposal,
    builtin_template_root,
    load_builtin_template,
    load_proposal,
    schema_fingerprint,
    validate_proposal,
)
from .materialize import (
    active_schema_fingerprint,
    has_knowledge_records,
    MaterializationResult,
    SchemaMaterializationError,
    materialize_schema,
    validate_materialized_schema,
    workspace_schema_status,
)

__all__ = [
    "SCIENTIFIC_ROLES",
    "SchemaModule",
    "SchemaPaths",
    "SchemaProposal",
    "active_schema_fingerprint",
    "builtin_template_root",
    "has_knowledge_records",
    "load_builtin_template",
    "load_proposal",
    "MaterializationResult",
    "SchemaMaterializationError",
    "materialize_schema",
    "schema_fingerprint",
    "validate_materialized_schema",
    "validate_proposal",
    "workspace_schema_status",
]
