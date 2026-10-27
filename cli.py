import argparse
import sys
from pathlib import Path
from reducer_core import reduce_project, generate_reduction_report
from symbol_reducer import remove_dead_symbols

def main():
    parser = argparse.ArgumentParser(description="Python Project Reducer CLI")
    parser.add_argument("--project", required=True, help="Path to target project directory")
    parser.add_argument("--entry", required=True, help="Entry point file or module")
    parser.add_argument("--output", required=True, help="Output directory for reduced project")
    parser.add_argument("--symbols", action="store_true", help="Apply symbol-level dead code removal on reachable files")
    
    args = parser.parse_args()
    
    project_dir = Path(args.project).resolve()
    entry_point = Path(args.entry)
    output_dir = Path(args.output).resolve()
    
    print(f"Analyzing project {project_dir} with entry point {entry_point}...")
    report = generate_reduction_report(project_dir, entry_point)
    print("Report:", report)
    
    copied = reduce_project(project_dir, entry_point, output_dir)
    print(f"Module-level reduction complete. Copied {len(copied)} files to {output_dir}")
    
    if args.symbols:
        print("Applying symbol-level dead code removal...")
        for p in output_dir.rglob("*.py"):
            try:
                cleaned = remove_dead_symbols(p)
                p.write_text(cleaned, encoding="utf-8")
            except Exception as e:
                print(f"Warning: could not process symbols for {p}: {e}")

if __name__ == "__main__":
    main()
