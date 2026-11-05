# Architecture

DGG-Agent organizes the editing workflow around explicit data structures and component interfaces. This separation keeps task inputs, editing plans, candidate references, and assessment records connected throughout an execution.

## Components

| Component | Interface | Responsibility |
| --- | --- | --- |
| Region provider | `RegionProvider.propose` | Return region references associated with an input task. |
| Planner | `Planner.plan` | Construct an editing plan from the request and region references. |
| Editor | `Editor.edit` | Consume the request and plan, and return a candidate reference. |
| Evaluator | `Evaluator.evaluate` | Return semantic and fidelity assessment records. |
| Memory | `MemoryStore.append` | Store the request, plan, candidate, and assessments together. |

## Data Structures

| Type | Fields |
| --- | --- |
| `EditRequest` | `task_id`, `source_path`, `instruction` |
| `EditPlan` | `target_text`, `region_refs` |
| `Candidate` | `task_id`, `image_ref` |
| `GateAssessment` | `name`, `status`, `note` |
| `RoundRecord` | `request`, `plan`, `candidate`, `assessments` |

Assessment statuses are represented by `PASS`, `FAIL`, `UNKNOWN`, and `ERROR`. The associated note provides context for the recorded assessment.

## Execution Flow

The pipeline receives its components through constructor arguments. A call to `run_once` performs the following steps:

1. Obtain region references for the input request.
2. Pass the request and region references to the planner.
3. Send the request and editing plan to the editor.
4. Evaluate the returned candidate.
5. Assemble a `RoundRecord` and append it to memory.
6. Return the record to the caller.

The task identifier connects the request and candidate. The round record retains the exact plan used for that call alongside its assessment results.

## Code Organization

- `contracts.py` defines the shared data structures.
- `interfaces.py` defines the component protocols.
- `pipeline.py` connects the components in execution order.
- `examples/dry_run.py` illustrates component wiring and JSON serialization.
