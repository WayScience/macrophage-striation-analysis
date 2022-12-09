from dataclasses import dataclass
from typing import Union


@dataclass(slots=True)
class ImageCropSelection:
    """Data structure containing metadata information of the selected
    cropped images. These are bounding boxes"""

    img_id: int
    x_coord: Union[int, float]
    y_coord: Union[int, float]
