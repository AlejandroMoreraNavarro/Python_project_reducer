import ast
from pathlib import Path
from typing import Set, Dict, Union

def analyze_symbols(file_path: Union[str, Path]) -> Dict[str, Set[str]]:
    """
    Analyse un fichier source Python et extrait les définitions (fonctions, classes)
    et les noms référencés (utilisés).
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
        
    tree = ast.parse(path.read_text(encoding="utf-8"))
    
    defined_functions: Set[str] = set()
    defined_classes: Set[str] = set()
    referenced_names: Set[str] = set()
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            defined_functions.add(node.name)
        elif isinstance(node, ast.ClassDef):
            defined_classes.add(node.name)
        elif isinstance(node, ast.Name):
            referenced_names.add(node.id)
            
    return {
        "functions": defined_functions,
        "classes": defined_classes,
        "referenced": referenced_names
    }
