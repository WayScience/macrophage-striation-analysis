from dataclasses import dataclass
from typing import Tuple, Union


@dataclass(slots=True)
class ImageCropSelection:
    """Data structure containing metadata information of the selected
    cropped images. These are bounding boxes"""

    img_id: int
    file_name: str
    crop_position: Tuple[int, int, int, int]
