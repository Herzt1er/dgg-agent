# DGG-Agent

DGG-Agent studies instruction-guided image editing through visual planning, region-aware editing, semantic assessment, fidelity assessment, and correction memory. The project connects these components through structured requests, editing plans, candidate references, and evaluation records.

## Overview

The workflow starts with a source image and a natural-language editing instruction. Region proposals provide spatial context for planning. An editing plan describes the target text and selected regions, while evaluation records capture semantic and fidelity assessments for subsequent analysis and feedback.

The architecture separates the responsibilities of each component:

- **Planning:** organize the editing instruction and region references into a structured plan.
- **Region selection:** identify the spatial references associated with the editing target.
- **Editing:** produce candidate outputs from the source and editing plan.
- **Semantic assessment:** assess instruction alignment and visual structure.
- **Fidelity assessment:** assess preservation of non-target content.
- **Correction memory:** organize editing states and assessment records across the workflow.

## Project Structure

```text
dgg-agent/
├── README.md
├── pyproject.toml
├── .gitignore
├── configs/
│   └── demo.json
├── docs/
│   └── architecture.md
├── examples/
│   └── dry_run.py
└── src/dgg_agent/
    ├── __init__.py
    ├── contracts.py
    ├── interfaces.py
    └── pipeline.py
```

## Quick Start

Use Python 3.10 or later. Run the example from the repository root:

```bash
python examples/dry_run.py
```

The example reads `configs/demo.json` and prints a structured record containing the request, plan, candidate reference, and assessments.

## Configuration

The example configuration contains three fields:

| Field | Description |
| --- | --- |
| `task_id` | Identifier for the editing task. |
| `source_path` | Reference to the source image. |
| `instruction` | Natural-language editing instruction. |

## Documentation

See [Architecture](docs/architecture.md) for component responsibilities, data structures, and the execution flow.
