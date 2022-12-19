"""
Module: paths.py

Contains data structures that allows where to load and write files into specific
directories.
"""

from pathlib import Path
from typing import Optional


class ProjectPaths:
    """Contains paths necessary to load or write files into"""

    def __init__(self, git_proj: Optional[bool] = True):
        self.root = None
        self.results = self.root / "results"
        self.git_proj = git_proj

    def _get_root_path(self) -> Path:
        """Obtains the project root path. If `git_proj` is True, it will search
        for a `.git` folder within the root project directory.

        Once the root folder is found, the function will set the `self.root`
        attribute with the absolute path pointing the root project directory

        Returns
        -------
        Path
            Absolute Path object pointing to the root project folder

        Raises
        ------
        TypeError
            Raised if `git_proj` is not a bool type
        FileNotFoundError
            Raised if the root project folder is found. If `git_proj` is true,
            then it will attempt to find both. If `git_proj` or root directory
            is not found, then it will raise a FileNotFound error
        """

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
