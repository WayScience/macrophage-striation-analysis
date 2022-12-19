"""
Module: image_utils.py


Contains functions that are used to analyze images.
"""

import itertools
from typing import List, Optional

from PIL import Image

from src.structs.selections import ImageCropSelection


def image_crop_walk(
    img_obj: Image,
    crop_width: int,
    crop_height: int,
    exact_size: Optional[bool] = True,
) -> List[ImageCropSelection]:
    """Takes in PIL image objects and traverse through the Image object

    Parameters
    ----------
    img_obj : PIL.Image
        Loaded PIL Image object
    crop_width : int
        crop width
    crop_height : int
        crop height
    exact_size : Optional[bool]
        Flag that indicates that only the provided size will be returned. PIL
        will return images of different crop sizes if the provided `crop_height`
        and `crop_width` do not split evenly to the source image size. Default
        is True

    Returns
    -------
    List[ImageCropSelection]
        List of ImageCropSelection object that contains, image_id, file_name,
        and cropping dimensions
    """
    # type checking
    # change to Path type if strin    # checking crop width inputs
    if not isinstance(img_obj, Image.Image):
        raise TypeError("img_obj must be PIL Image object")
    if not isinstance(crop_height, int):
        raise TypeError(f"'crop_height' must integer not {type(crop_height)}")
    if not isinstance(crop_width, int):
        raise TypeError(f"'crop_width' must integer not {type(crop_height)}")

    # setting up cropping dimensions
    width, height = img_obj.size
    width_range_crop = range(0, width, crop_width)
    height_range_crop = range(0, height, crop_height)

    # -- this will store image information indicating which images were selected
    # -- based on
    # NOTE: make sure to download crop size, source, and id
    list_of_cropped_images = []
    for frame_num, (col_i, row_i) in enumerate(
        itertools.product(width_range_crop, height_range_crop), start=1
    ):

        # create a crop object with given dimensions
        crop = img_obj.crop((col_i, row_i, col_i + crop_width, row_i + crop_height))

        # checking if the crop size is exact, if not skip
        crop_size = crop.size
        if exact_size is True and (crop_width, crop_height) != crop_size:
            continue

        # convert to ImageCropSelection Object
        sel_obj = ImageCropSelection(
            img_id=frame_num,
            file_name=img_obj.filename,
            img_size=crop_size,
            crop_position=(
                col_i,
                row_i,
                col_i + crop_width,
                row_i + crop_height,
            ),
        )

        list_of_cropped_images.append(sel_obj)

    return list_of_cropped_images
