import ast
from pathlib import Path
from typing import Union, Set
from symbol_analyzer import analyze_symbols

class DeadCodeRemover(ast.NodeTransformer):
    def __init__(self, unused_funcs: Set[str], unused_classes: Set[str]):
        self.unused_funcs = unused_funcs
        self.unused_classes = unused_classes

    def visit_FunctionDef(self, node):
        if node.name in self.unused_funcs:
            return None
        return self.generic_visit(node)

    def visit_ClassDef(self, node):
        if node.name in self.unused_classes:
            return None
        return self.generic_visit(node)

def remove_dead_symbols(file_path: Union[str, Path]) -> str:
    """
    Analyse le fichier, identifie les classes et fonctions non référencées,
    et renvoie le code source réécrit sans ces symboles morts.
    """
    path = Path(file_path)
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    
    analysis = analyze_symbols(path)
    referenced = analysis["referenced"]
    
    unused_funcs = analysis["functions"] - referenced
    unused_classes = analysis["classes"] - referenced
    
    transformer = DeadCodeRemover(unused_funcs, unused_classes)
    new_tree = transformer.visit(tree)
    ast.fix_missing_locations(new_tree)
    
    return ast.unparse(new_tree)
