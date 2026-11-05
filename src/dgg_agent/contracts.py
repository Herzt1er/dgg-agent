"""Data structures for editing requests, plans, candidates, and assessments."""

from dataclasses import dataclass
from enum import Enum


class GateStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNKNOWN = "UNKNOWN"
    ERROR = "ERROR"


@dataclass(frozen=True)
class EditRequest:
    task_id: str
    source_path: str
    instruction: str


@dataclass(frozen=True)
class EditPlan:
    target_text: str
    region_refs: tuple[str, ...] = ()


@dataclass(frozen=True)
class Candidate:
    task_id: str
    image_ref: str


@dataclass(frozen=True)
class GateAssessment:
    name: str
    status: GateStatus
    note: str


@dataclass(frozen=True)
class RoundRecord:
    request: EditRequest
    plan: EditPlan
    candidate: Candidate
    assessments: tuple[GateAssessment, ...]
