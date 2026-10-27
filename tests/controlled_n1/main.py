from tests.controlled_n1 import dead_code

def feature_useful() -> int:
    # Utilise dead_code pour qu'il soit importé mais jamais appelé
    _ = dead_code.feature_dead()
    return 42
