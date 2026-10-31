import shutil
from pathlib import Path
from typing import List, Dict, Any
from intent_analyzer import IntentAnalyzer

class IntentReducer:
    """Reduces a project by keeping only modules related to desired features."""
    def __init__(self, project_dir: str, output_dir: str, desired_features: List[str]):
        self.project_dir = Path(project_dir)
        self.output_dir = Path(output_dir)
        self.analyzer = IntentAnalyzer(project_dir, desired_features)

    def reduce(self) -> Dict[str, Any]:
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        all_files = [p.name for p in self.project_dir.glob("*.py") if p.is_file()]
        retained = self.analyzer.filter_modules(all_files)
        removed = [f for f in all_files if f not in retained]

        for file_name in retained:
            src_path = self.project_dir / file_name
            if src_path.exists():
                shutil.copy(src_path, self.output_dir / file_name)

        return {
            "retained": retained,
            "removed": removed
        }
