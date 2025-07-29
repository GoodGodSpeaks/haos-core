import json
from pathlib import Path

def main():
    concept = {
        "concept_id": "demo001",
        "design_parameters": {
            "plasma_radius": 1.0,
            "coil_current": 5e6
        }
    }
    out_path = Path(__file__).resolve().parents[2] / "run_data" / "concept_spec_v1.json"
    out_path.write_text(json.dumps(concept, indent=2))
    print(f"✅ Planner: Concept Spec written to {out_path}")

if __name__ == "__main__":
    main()
