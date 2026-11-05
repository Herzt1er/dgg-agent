"""Example of component wiring and record serialization."""

import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dgg_agent.contracts import Candidate, EditPlan, EditRequest, GateAssessment, GateStatus
from dgg_agent.pipeline import ScaffoldPipeline


class DemoRegions:
    def propose(self, request):
        return ("demo://region-placeholder",)


class DemoPlanner:
    def plan(self, request, region_refs):
        return EditPlan(request.instruction, region_refs)


class DemoEditor:
    def edit(self, request, plan):
        return Candidate(request.task_id, "demo://no-image-generated")


class DemoEvaluator:
    def evaluate(self, request, candidate):
        return tuple(
            GateAssessment(name, GateStatus.UNKNOWN, "Mock only; no evaluation performed.")
            for name in ("semantic", "fidelity")
        )


class DemoMemory:
    def __init__(self):
        self.records = []

    def append(self, record):
        self.records.append(record)


def main():
    request = EditRequest(**json.loads((ROOT / "configs" / "demo.json").read_text(encoding="utf-8")))
    pipeline = ScaffoldPipeline(DemoRegions(), DemoPlanner(), DemoEditor(), DemoEvaluator(), DemoMemory())
    record = pipeline.run_once(request)
    print(json.dumps({"demo_only": True, "record": asdict(record)}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
