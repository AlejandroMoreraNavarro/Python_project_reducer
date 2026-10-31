import pytest
import sys
from pathlib import Path
from intent_reducer import IntentReducer

def test_intent_reducer_execution_e2e():
    project_dir = "tests/controlled_v2"
    output_dir = "work/controlled_v2_reduced"
    
    reducer = IntentReducer(project_dir, output_dir, desired_features=["feature_a"])
    report = reducer.reduce()
    
    assert "feature_a.py" in report["retained"]
    assert "feature_b.py" in report["removed"]
    
    # Verify files on disk
    assert (Path(output_dir) / "feature_a.py").exists()
    assert not (Path(output_dir) / "feature_b.py").exists()
    
    # E2E functional verification
    sys.path.insert(0, str(Path(output_dir).resolve()))
    import feature_a
    assert feature_a.feature_a_logic() == "Feature A executed"
    sys.path.pop(0)
