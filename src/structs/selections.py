"""
Module: selection.py

Contains data structure and functions that focuses on obtaining metadata
from cropped images.
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass(slots=True)
class ImageCropSelection:
    """Data structure containing metadata information of the selected
    cropped images.


    Attributes:
    -----------
    img_id : int
        unique number id that represents the cropped image

    file_name : str
        Name of the file where the cropped image came from.

    image_size : tuple [int, int]
        Image crop size

    crop_position : tuple[int, int, int, int]
        The crop position used to select cropped image

    __classification : None [Private attribute]
        This attribute is initialized as a private attribute used for declaring
        whether the cropped image is either positive or negative for a specific
        characterization. By default it will be set a "None" indicating that no
        classification has been performed to the specific cropped image. 

    """

    img_id: int
    file_name: str
    img_size: tuple[int, int]
    crop_position: tuple[int, int, int, int]
    
    # private attribute
    __classification = None
    

    def to_dict(self) -> dict:
        """Converts `ImageCropSelection` entry into a dictionary type"""
        return dict(
            img_id=self.img_id,
            file_name=self.file_name,
            img_size=self.img_size,
            crop_position=self.crop_position,
            classification=self.__classification
        )
