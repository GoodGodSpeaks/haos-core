import json
from pathlib import Path

def main():
    base = Path(__file__).resolve().parents[2] / "run_data"
    spec = json.loads((base / "concept_spec_v1.json").read_text())
    radius = spec["design_parameters"]["plasma_radius"]
    current = spec["design_parameters"]["coil_current"]
    B_field = current / radius
    (base / "domain_kpi_v1.json").write_text(json.dumps({ "B_field_estimated": B_field }, indent=2))
    print(f"✅ DummySim: Estimated B_field = {B_field}")

if __name__ == "__main__":
    main()
