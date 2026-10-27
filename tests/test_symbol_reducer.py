from pathlib import Path
from symbol_analyzer import analyze_symbols

def test_analyze_symbols(tmp_path):
    # Création d'un module de test temporaire avec des fonctions utilisées et inutilisées
    test_file = tmp_path / "sample.py"
    test_file.write_text("""
class UsedClass:
    pass

class UnusedClass:
    pass

def used_func():
    return UsedClass()

def unused_func():
    return "dead"

result = used_func()
""", encoding="utf-8")

    analysis = analyze_symbols(test_file)
    
    assert "UsedClass" in analysis["classes"]
    assert "UnusedClass" in analysis["classes"]
    assert "used_func" in analysis["functions"]
    assert "unused_func" in analysis["functions"]
    
    assert "used_func" in analysis["referenced"]
    assert "UsedClass" in analysis["referenced"]
