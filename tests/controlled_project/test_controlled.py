from tests.controlled_project.main import run_app

def test_run_app():
    result = run_app()
    assert result["shared"] == "shared utility active"
    assert result["plugin"] == "plugin a executed"
    assert "config_value: 100" in result["resource"]
