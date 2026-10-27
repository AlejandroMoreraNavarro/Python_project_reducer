from pathlib import Path
from tests.controlled_project.shared import shared_utility
from tests.controlled_project.registry import REGISTRY
from tests.controlled_project.dynamic_loader import load_dynamic_module

# Dépendance optionnelle gérée
try:
    import optional_pkg
    HAS_OPTIONAL = True
except ImportError:
    HAS_OPTIONAL = False

def run_app() -> dict:
    # Lire la ressource
    res_path = Path(__file__).parent / "resource.txt"
    res_content = res_path.read_text(encoding="utf-8") if res_path.exists() else ""
    
    # Utiliser le module partagé
    shared_res = shared_utility()
    
    # Utiliser le registre
    plugin_func = REGISTRY.get("plugin_a")
    plugin_res = plugin_func() if plugin_func else "no plugin"
    
    return {
        "shared": shared_res,
        "plugin": plugin_res,
        "has_optional": HAS_OPTIONAL,
        "resource": res_content.strip()
    }

if __name__ == "__main__":
    print(run_app())
