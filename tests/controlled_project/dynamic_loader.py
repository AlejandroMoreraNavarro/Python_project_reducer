import importlib

def load_dynamic_module(module_name: str):
    mod = importlib.import_module(module_name)
    return mod
