import ast
from pathlib import Path
from typing import Set, List, Union

def find_reachable_modules(project_dir: Union[str, Path], entry_point: Union[str, Path]) -> Set[Path]:
    """
    Parcourt statiquement les imports à partir d'un point d'entrée dans un dossier de projet
    et renvoie l'ensemble des chemins de fichiers .py atteignables.
    """
    root = Path(project_dir).resolve()
    entry = Path(entry_point)
    if not entry.is_absolute():
        candidate = (root / entry).resolve()
        if candidate.exists():
            entry = candidate
        else:
            entry = (Path.cwd() / entry_point).resolve()

    print(f"DEBUG: root={root}, entry={entry}, exists={entry.exists()}")

    if not entry.exists():
        raise FileNotFoundError(f"Entry point {entry_point} not found relative to project {root}")

    visited: Set[Path] = set()
    queue: List[Path] = [entry]

    while queue:
        current_file = queue.pop(0)
        if current_file in visited:
            continue
        try:
            rel = current_file.relative_to(root)
        except ValueError:
            print(f"DEBUG: {current_file} is not relative to root {root}")
            continue
            
        visited.add(current_file)
        print(f"DEBUG: visiting {current_file}")
        
        try:
            tree = ast.parse(current_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        for node in ast.walk(tree):
            imported_files = []
            if isinstance(node, ast.Import):
                for alias in node.names:
                    mod_path = _resolve_module_to_path(root, current_file, alias.name)
                    if mod_path:
                        imported_files.append(mod_path)
            elif isinstance(node, ast.ImportFrom):
                if node.level > 0:
                    # Relative import
                    mod_path = _resolve_relative_import(root, current_file, node.module, node.level)
                    if mod_path:
                        imported_files.append(mod_path)
                elif node.module:
                    mod_path = _resolve_module_to_path(root, current_file, node.module)
                    if mod_path:
                        imported_files.append(mod_path)
                    # Also check if names imported are submodule files
                    for alias in node.names:
                        sub_path = _resolve_module_to_path(root, current_file, f"{node.module}.{alias.name}")
                        if sub_path:
                            imported_files.append(sub_path)

            for mf in imported_files:
                if mf not in visited and mf.exists():
                    queue.append(mf)

    return visited

def _resolve_module_to_path(root: Path, current_file: Path, module_name: str) -> Path:
    parts = module_name.split('.')
    # Try direct parts
    candidate = root / Path(*parts).with_suffix('.py')
    if candidate.exists():
        return candidate
    candidate_init = root / Path(*parts) / '__init__.py'
    if candidate_init.exists():
        return candidate_init

    # Try stripping leading package components if they match root name or parents
    for i in range(1, len(parts)):
        sub_parts = parts[i:]
        candidate = root / Path(*sub_parts).with_suffix('.py')
        if candidate.exists():
            return candidate
        candidate_init = root / Path(*sub_parts) / '__init__.py'
        if candidate_init.exists():
            return candidate_init

    # Search by filename across root
    target_name = parts[-1] + '.py'
    matches = list(root.rglob(target_name))
    if matches:
        return matches[0]

    return None

def _resolve_relative_import(root: Path, current_file: Path, module_name: str, level: int) -> Path:
    base_dir = current_file.parent
    for _ in range(level - 1):
        base_dir = base_dir.parent
    if module_name:
        parts = module_name.split('.')
        candidate = base_dir / Path(*parts).with_suffix('.py')
        if candidate.exists():
            return candidate
        candidate_init = base_dir / Path(*parts) / '__init__.py'
        if candidate_init.exists():
            return candidate_init
    else:
        # from . import foo handled via names
        pass
    return None
