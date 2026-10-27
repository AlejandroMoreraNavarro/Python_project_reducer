from pathlib import Path
from reducer_core import find_reachable_modules

def test_find_reachable_modules_controlled():
    project_dir = Path("tests/controlled_project").resolve()
    entry_point = project_dir / "main.py"
    
    reachable = find_reachable_modules(project_dir, entry_point)
    
    relative_reachable = {p.relative_to(project_dir).as_posix() for p in reachable}
    
    assert "main.py" in relative_reachable
    assert "shared.py" in relative_reachable
    assert "registry.py" in relative_reachable
    
    print(f"Reachable files: {relative_reachable}")
