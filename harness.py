import subprocess
import sys
import os
import shutil
from pathlib import Path

def run_project(script_path: Path, pythonpath: str) -> tuple[int, str, str]:
    env = dict(os.environ)
    env["PYTHONPATH"] = pythonpath
    cmd = [sys.executable, str(script_path)]
    res = subprocess.run(cmd, capture_output=True, text=True, env=env)
    return res.returncode, res.stdout, res.stderr

def compare_outputs(orig_script: Path, orig_pp: str, copy_script: Path, copy_pp: str) -> dict:
    code_orig, out_orig, err_orig = run_project(orig_script, orig_pp)
    code_copy, out_copy, err_copy = run_project(copy_script, copy_pp)
    
    return {
        "returncode_match": code_orig == code_copy,
        "stdout_match": out_orig.strip() == out_copy.strip(),
        "stderr_match": err_orig == err_copy,
        "orig_out": out_orig.strip(),
        "copy_out": out_copy.strip()
    }

def run_meta_regression_tests() -> int:
    """Injects at least 3 regressions and verifies the harness detects them."""
    orig_script = Path("tests/controlled_project/main.py")
    orig_pp = "."
    
    work_base = Path("work/controlled_project_test")
    work_copy_dir = work_base / "tests" / "controlled_project"
    copy_script = work_copy_dir / "main.py"
    copy_pp = str(work_base)
    
    if work_base.exists():
        shutil.rmtree(work_base)
    
    work_copy_dir.mkdir(parents=True, exist_ok=True)
    for item in Path("tests/controlled_project").iterdir():
        if item.is_file():
            shutil.copy2(item, work_copy_dir / item.name)
            
    detections = 0
    
    # Regression 1: Break shared utility in main.py
    main_path = copy_script
    orig_main = main_path.read_text(encoding="utf-8")
    main_path.write_text(orig_main.replace("shared_utility()", "'broken_shared'"), encoding="utf-8")
    
    res1 = compare_outputs(orig_script, orig_pp, copy_script, copy_pp)
    if not res1["stdout_match"]:
        detections += 1
        print("Regression 1 (broken shared output) successfully detected!")
    
    # Reset
    main_path.write_text(orig_main, encoding="utf-8")
    
    # Regression 2: Break resource file content
    res_path = work_copy_dir / "resource.txt"
    orig_res = res_path.read_text(encoding="utf-8")
    res_path.write_text("config_value: 999\n", encoding="utf-8")
    
    res2 = compare_outputs(orig_script, orig_pp, copy_script, copy_pp)
    if not res2["stdout_match"]:
        detections += 1
        print("Regression 2 (broken resource config) successfully detected!")
        
    res_path.write_text(orig_res, encoding="utf-8")
    
    # Regression 3: Break registry plugin
    reg_path = work_copy_dir / "registry.py"
    orig_reg = reg_path.read_text(encoding="utf-8")
    reg_path.write_text(orig_reg.replace('"plugin a executed"', '"broken plugin"'), encoding="utf-8")
    
    res3 = compare_outputs(orig_script, orig_pp, copy_script, copy_pp)
    if not res3["stdout_match"]:
        detections += 1
        print("Regression 3 (broken registry plugin) successfully detected!")
        
    reg_path.write_text(orig_reg, encoding="utf-8")
    
    # Cleanup
    if work_base.exists():
        shutil.rmtree(work_base)
        
    print(f"Total meta-regressions detected: {detections}/3")
    return detections

if __name__ == "__main__":
    detects = run_meta_regression_tests()
    if detects >= 3:
        print("SUCCESS: Harness reliably detects 3/3 regressions.")
        sys.exit(0)
    else:
        print("FAILURE: Harness did not detect all regressions.")
        sys.exit(1)
