from pathlib import Path
import agents.planner.main as planner
import agents.dummy_sim.main as dummy
import agents.aggregator.main as aggregator

def test_agent_pipeline():
    run_data = Path(__file__).resolve().parents[1] / "run_data"
    run_data.mkdir(exist_ok=True)

    planner.main()
    dummy.main()
    aggregator.main()

    assert (run_data / "concept_spec_v1.json").exists()
    assert (run_data / "domain_kpi_v1.json").exists()
