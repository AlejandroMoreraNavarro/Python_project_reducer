import ast
from pathlib import Path
from typing import List, Set

class IntentAnalyzer:
    """Analyzes a project to filter files/symbols based on desired features."""
    def __init__(self, project_dir: str, desired_features: List[str]):
        self.project_dir = Path(project_dir)
        self.desired_features = set(desired_features)

    def filter_modules(self, available_modules: List[str]) -> List[str]:
        """Filters modules to retain only those matching desired features or core."""
        filtered = []
        for mod in available_modules:
            # If module name matches any desired feature or is general (main)
            if any(feat in mod for feat in self.desired_features) or "main" in mod or "shared" in mod:
                filtered.append(mod)
        return filtered
