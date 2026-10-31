import sys
import ast
from pathlib import Path

def analyze_project(project_path: str):
    root = Path(project_path)
    if not root.exists():
        print(f"Path {root} does not exist.")
        return

    print(f"--- Analyzing Python files in {root} ---")
    py_files = list(root.rglob("*.py"))
    for py_file in py_files:
        print(f"\nFile: {py_file}")
        try:
            tree = ast.parse(py_file.read_text(encoding="utf-8"))
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)
            print(f"  Imports: {imports}")
        except Exception as e:
            print(f"  Error parsing: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_project(sys.argv[1])
    else:
        print("Usage: python reducer.py <project_dir>")
