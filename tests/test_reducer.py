from pathlib import Path
from reducer_core import find_reachable_modules, reduce_project, compute_dir_hash, generate_reduction_report

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
    
    hash_before = compute_dir_hash(project_dir)
    reduce_project(project_dir, entry_point, output_dir)
    hash_after = compute_dir_hash(project_dir)
    
    assert hash_before == hash_after, "Original project was modified during reduction!"
    
    reduced_files = {p.relative_to(output_dir).as_posix() for p in output_dir.rglob("*.py")}
    
    assert "main.py" in reduced_files
    assert "shared.py" in reduced_files
    assert "registry.py" in reduced_files
    assert "unimported_module.py" not in reduced_files

def test_generate_reduction_report():
    project_dir = Path("tests/controlled_project").resolve()
    entry_point = project_dir / "main.py"
    
    report = generate_reduction_report(project_dir, entry_point)
    
    assert "necessary" in report
    assert "precaution" in report
    assert "removed" in report
    assert "uncertain" in report
    
    assert "main.py" in report["necessary"]
    assert "resource.txt" in report["precaution"]
    assert "unimported_module.py" in report["removed"]
    assert "dynamic_loader.py" in report["uncertain"]
