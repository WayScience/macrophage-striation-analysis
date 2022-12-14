"""
Module: selection.py

Contains data structure and functions that focuses on obtaining metadata
from cropped images.
"""
from dataclasses import dataclass
from typing import Any, Dict, Tuple


@dataclass(slots=True)
class ImageCropSelection:
    """Data structure containing metadata information of the selected
    cropped images."""

    img_id: int
    file_name: str
    img_size: tuple[int, int]
    crop_position: Tuple[int, int, int, int]

    def to_dict(self) -> dict:
        """Converts `ImageCropSelection` entry into a dictionary type"""
        return dict(
            img_id=self.img_id,
            file_name=self.file_name,
            img_size=self.img_size,
            crop_position=self.crop_position,
        )
