"""
module: arrays_guards.py

Module that support strict type checking. This focuses on check the array types
and elements within
"""
from typing import List, Tuple, TypeGuard

from src.structs.selections import ImageCropSelection


def is_list_of_crop_selections(
    array: object,
) -> TypeGuard[List[ImageCropSelection]]:
    """Checks if the array contains only ImageCropSelection objects.

    Returns
    -------
    TypeGuard[List[ImageCropSelection]]
        Ensures that the list provided is all ImageCropSelection objects
    """
    # only accepts tuples or lists
    accepted_types = (List, Tuple)

    # checking for both array and element types
    return (
        all(isinstance(elm, ImageCropSelection) for elm in array)
        if isinstance(array, accepted_types)
        else False
    )
