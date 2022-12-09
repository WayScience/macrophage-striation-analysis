"""
Module: paths.py

Contains data structures that
"""

from pathlib import Path
from typing import Optional


class ProjectPaths:
    def __init__(self, git_proj: Optional[bool] = True):
        self.root = None
        self.results = self.root / "results"
        self.git_proj = git_proj

    def _get_root_path(self) -> Path:

        # type checking
        if not isinstance(self.git_proj, bool):
            _type = type(self.git_proj)
            raise TypeError(f"'git_proj' must be a boolean type not {_type}")

        # searching project root folder
        proj_root_name = "macrophage-striation-analysis"
        path_list = __file__.rsplit(proj_root_name, 1)
        if len(path_list) <= 1:
            raise FileNotFoundError("Unable to find project root folder")

        # build the path
        root_path = Path(path_list[0]) / proj_root_name

        # checking '.git' folder
        if self.git_proj:
            check = (root_path / ".git").exists()
            if check is False:
                raise FileNotFoundError("Unable to find project root folder")

        self.root = root_path
        return self.root
