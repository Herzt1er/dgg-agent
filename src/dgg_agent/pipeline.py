"""Single-pass component orchestration."""

from dataclasses import dataclass

from .contracts import EditRequest, RoundRecord
from .interfaces import Editor, Evaluator, MemoryStore, Planner, RegionProvider


@dataclass
class ScaffoldPipeline:
    regions: RegionProvider
    planner: Planner
    editor: Editor
    evaluator: Evaluator
    memory: MemoryStore

    def run_once(self, request: EditRequest) -> RoundRecord:
        region_refs = self.regions.propose(request)
        plan = self.planner.plan(request, region_refs)
        candidate = self.editor.edit(request, plan)
        assessments = self.evaluator.evaluate(request, candidate)
        record = RoundRecord(request, plan, candidate, assessments)
        self.memory.append(record)
        return record
