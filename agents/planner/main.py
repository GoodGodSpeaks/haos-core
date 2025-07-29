import json
from pathlib import Path
from jsonschema import validate, ValidationError

def main():
    concept = {
        "concept_id": "demo001",
        "design_parameters": {
            "plasma_radius": 1.0,
            "coil_current": 5e6
        }
    }

    # Validate against schema
    base = Path(__file__).resolve().parents[2]
    schema_path = base / "shared" / "json_schemas" / "concept_spec_v1.json"
    schema = json.loads(schema_path.read_text())

    try:
        validate(instance=concept, schema=schema)
        print("✅ Planner: Output schema is valid.")
    except ValidationError as e:
        print("❌ Schema validation error:", e)
        return

    output_path = base / "run_data" / "concept_spec_v1.json"
    output_path.write_text(json.dumps(concept, indent=2))
    print(f"✅ Planner: Concept Spec written to {output_path}")

if __name__ == "__main__":
    main()
