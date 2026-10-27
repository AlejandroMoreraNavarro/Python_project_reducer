from pathlib import Path
from reducer_core import find_reachable_modules, reduce_project, compute_dir_hash

def test_find_reachable_modules_controlled():
    project_dir = Path("tests/controlled_project").resolve()
    entry_point = project_dir / "main.py"
    
    reachable = find_reachable_modules(project_dir, entry_point)
    relative_reachable = {p.relative_to(project_dir).as_posix() for p in reachable}
    
    assert "main.py" in relative_reachable
    assert "shared.py" in relative_reachable
    assert "registry.py" in relative_reachable

def test_reduce_project_and_integrity():
    project_dir = Path("tests/controlled_project").resolve()
    entry_point = project_dir / "main.py"
    output_dir = Path("work/controlled_reduced").resolve()
    
    # 1. Compute hash of original before reduction
    hash_before = compute_dir_hash(project_dir)
    
    # 2. Run reduction / copy
    copied = reduce_project(project_dir, entry_point, output_dir)
    
    # 3. Compute hash of original after reduction to ensure it remains strictly intact
    hash_after = compute_dir_hash(project_dir)
    
    assert hash_before == hash_after, "Original project was modified during reduction!"
    
    # 4. Verify reduced output contains expected files and excludes unreached ones (e.g. unimported_module.py)
    reduced_files = {p.relative_to(output_dir).as_posix() for p in output_dir.rglob("*.py")}
    
    assert "main.py" in reduced_files
    assert "shared.py" in reduced_files
    assert "registry.py" in reduced_files
    assert "unimported_module.py" not in reduced_files
