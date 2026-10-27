import ast
from pathlib import Path
from symbol_analyzer import analyze_symbols
from symbol_reducer import remove_dead_symbols

def test_analyze_symbols(tmp_path):
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

def test_remove_dead_symbols(tmp_path):
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

    rewritten_code = remove_dead_symbols(test_file)
    
    assert "used_func" in rewritten_code
    assert "UsedClass" in rewritten_code
    assert "unused_func" not in rewritten_code
    assert "UnusedClass" not in rewritten_code
    
    # Verify the rewritten code is syntactically valid Python
    ast.parse(rewritten_code)
