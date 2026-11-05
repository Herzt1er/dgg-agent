"""Component interfaces for the image editing workflow."""

from typing import Protocol

from .contracts import Candidate, EditPlan, EditRequest, GateAssessment, RoundRecord


class RegionProvider(Protocol):
    def propose(self, request: EditRequest) -> tuple[str, ...]: ...


class Planner(Protocol):
    def plan(self, request: EditRequest, region_refs: tuple[str, ...]) -> EditPlan: ...


class Editor(Protocol):
    def edit(self, request: EditRequest, plan: EditPlan) -> Candidate: ...


class Evaluator(Protocol):
    def evaluate(self, request: EditRequest, candidate: Candidate) -> tuple[GateAssessment, ...]: ...


class MemoryStore(Protocol):
    def append(self, record: RoundRecord) -> None: ...
