from pathlib import Path
from reducer_core import reduce_project, generate_reduction_report

def main():
    project_dir = Path("external/pypdf").resolve()
    # Entrée représentative : pypdf/__init__.py ou pypdf/_reader.py
    entry_point = project_dir / "pypdf" / "__init__.py"
    output_dir = Path("work/pypdf_reduced").resolve()
    
    print(f"Running reduction on pypdf from {entry_point}...")
    
    report = generate_reduction_report(project_dir, entry_point)
    print("Reduction Report Summary:")
    print(f"  Necessary (reachable .py): {len(report['necessary'])}")
    print(f"  Precaution (non-.py/aux): {len(report['precaution'])}")
    print(f"  Removed (unreachable .py): {len(report['removed'])}")
    print(f"  Uncertain: {len(report['uncertain'])}")
    
    copied = reduce_project(project_dir, entry_point, output_dir)
    print(f"Reduced pypdf generated at {output_dir}. Total files copied: {len(copied)}")

if __name__ == "__main__":
    main()
