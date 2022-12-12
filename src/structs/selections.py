from dataclasses import dataclass
from typing import Tuple, Union


@dataclass(slots=True)
class ImageCropSelection:
    """Data structure containing metadata information of the selected
    cropped images.

    Parameters: 
    -----------
    crop_id : int
        unique id of cropped image data:
    file_source : str
        Where the cropped image was taken from
    crop_position: Tuple[int, int, int, int]
        Contains the left, top, right and bottom positional values

    Returns
    -------
    Self
        ImageCropSelection, dataclass that contains metadata of the
        cropped image.
    """
    crop_id: int
    file_source: str
    crop_position: Tuple[int, int, int, int]
