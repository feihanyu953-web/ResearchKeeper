"""Fail-closed policy checks for audit deferrals."""

from __future__ import annotations

import re
from typing import Mapping


_GENERIC_REASONS = re.compile(
    r"(?:time\s+(?:is\s+)?(?:short|insufficient)|too\s+(?:large|complex)|"
    r"时间不够|改动太大|复杂度高)",
    flags=re.IGNORECASE,
)


def _non_empty_list(value: object) -> bool:
    return isinstance(value, (list, tuple)) and any(
        str(item).strip() for item in value
    )


def validate_non_blocking_request(
    *,
    failed_rounds: int,
    justifications: Mapping[str, Mapping[str, object]],
    reviewer_log_written: bool,
    user_confirmed: bool,
) -> list[str]:
    """Return contract violations for a requested NON-BLOCKING deferral."""
    errors: list[str] = []
    if failed_rounds < 3:
        errors.append("requires at least 3 failed audit rounds")
    if not justifications:
        errors.append("at least one failed item justification is required")

    for item, justification in sorted(justifications.items()):
        reason = str(justification.get("technical_reason", "")).strip()
        specific_reason = _GENERIC_REASONS.sub("", reason).strip(
            " \t\r\n,.;:，。；："
        )
        if not specific_reason:
            errors.append(f"{item}: specific technical_reason is required")
        if not _non_empty_list(justification.get("attempted_fixes")):
            errors.append(f"{item}: attempted_fixes are required")
        if not str(justification.get("remaining_risk", "")).strip():
            errors.append(f"{item}: remaining_risk is required")
        if not (
            _non_empty_list(justification.get("files"))
            and _non_empty_list(justification.get("evidence"))
        ):
            errors.append(f"{item}: files and evidence are required")

    if not reviewer_log_written:
        errors.append("reviewer log was not written")
    if not user_confirmed:
        errors.append("explicit user confirmation is missing")
    return errors
