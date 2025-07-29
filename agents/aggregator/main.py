import json
from pathlib import Path

def main():
    base = Path(__file__).resolve().parents[2] / "run_data"
    result = json.loads((base / "domain_kpi_v1.json").read_text())
    print(f"✅ Aggregator: Final KPI = {result}")

if __name__ == "__main__":
    main()
