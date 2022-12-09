"""
module: arrays_guards.py

Module that support strict type checking. This focuses on check the array types
and elements within
"""
from src.structs.selections import ImageCropSelection


def is_array_of_coords(arr: object) -> bool:
    """Checks if the given object is an array of ImageCropSelection"""

    accepted_array_types = (tuple, list)
    return (
        all(isinstance(elm, ImageCropSelection) for elm in arr)
        if isinstance(arr, accepted_array_types)
        else False
    )
