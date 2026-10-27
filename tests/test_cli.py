import subprocess
import sys
from pathlib import Path

def test_cli_execution(tmp_path):
    project_dir = Path("tests/controlled_project").resolve()
    entry_point = project_dir / "main.py"
    output_dir = tmp_path / "reduced_output"
    
    cmd = [
        sys.executable,
        "cli.py",
        "--project", str(project_dir),
        "--entry", str(entry_point),
        "--output", str(output_dir),
        "--symbols"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    assert result.returncode == 0, f"CLI failed with stderr: {result.stderr}"
    assert "Module-level reduction complete" in result.stdout
    assert output_dir.exists()
    assert (output_dir / "main.py").exists()
    assert (output_dir / "shared.py").exists()
