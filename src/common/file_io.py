"""
module: file_io.py

Module that contains functions responsible for moving, creating, writing and
deleting files in the current directory.
"""
import json
from collections import defaultdict
from pathlib import Path
from typing import Iterator, List, Optional

from PIL import Image

from src.guards.arrays_guards import is_list_of_crop_selections
from src.structs.selections import ImageCropSelection


def load_tiff_images(
    img_dir: str | Path,
) -> Iterator[Image.Image]:
    """Loads images from given directory. Returns a list of PIL Image objects

    Parameters
    ----------
    img_dir : str | Path
       directory path containing image paths

    Returns
    -------
    Iterator[Image.Image]
        Python generator that returns PIL Image objects

    Raises
    ------
    FileNotFoundError
        Raised if the 'img_dir' does not exist
    TypeError
        Raised if images are not in `tiff` format
        Raised if `img_dir` is not str or Path type
    """

    # type checking
    # -- if str type, convert to Path type
    accepted_types = (str, Path)
    if not isinstance(img_dir, accepted_types):
        _type = type(img_dir)
        raise TypeError(f"'fpath' must str or path type not {_type}")
    if isinstance(img_dir, str):
        img_dir = Path(img_dir)

    # check if the file exists
    if not img_dir.exists():
        raise FileNotFoundError(f"Unable to find: {str(img_dir)}")

    # check if it is a directory
    if not img_dir.is_dir():
        raise TypeError("`img_dir` must be a directory")

    # grab all .tiff images within given image directory
    tiff_paths = list(img_dir.glob("*.tiff"))
    if not tiff_paths:
        raise FileNotFoundError("Unable to find '.tiff' images in `img_dir`")

    # loading images into memory
    # -- List[Tuple(path/to/image, PIL Image Object)]
    for tiff_path in tiff_paths:
        yield Image.open(tiff_path)


def coord_to_json(
    cord_array: List[ImageCropSelection],
    outname: Optional[str] = "image_cords",
):
    """Writes array of `ImageCropSelection`s into a JSON file format.

    Parameters
    ----------
    cord_array: List[ImageCropSelection]
        Array containing `ImageCropSelection`
    outname : Optional, optional
        Path to save output, by default "./"


    Return
    ------
    Path
        Returns path object where the json file was saved
    """

    # type checking out_path
    accepted_path_types = (str, Path)
    if not isinstance(outname, accepted_path_types):
        raise TypeError("'out_path' must be str or Path type")
    if isinstance(outname, str):
        outname = Path(outname).absolute()

    # checking if out_path contains nested directories
    out_path_parent_dir = outname.parent
    if not out_path_parent_dir.exists():
        out_path_parent_dir.mkdir(parent=True, exist_ok=True)

    # extracting coordinate data
    cord_data = defaultdict(list)
    for grouped_imgs in cord_array:

        # checking if provided array is list of `ImageCropSelection`s
        if not is_list_of_crop_selections(grouped_imgs):
            raise TypeError(
                "'coord_array' must be an array of 'ImageCropSelection' objects"
            )

        # iterating through every crop entry and store crop metadata to dict
        for crop_entry in grouped_imgs:
            meta_data_dict = crop_entry.to_dict()
            file_name = str(Path(crop_entry.file_name).name)
            cord_data[file_name].append(meta_data_dict)

    # saving coordinates into JSON file
    save_path = Path("./") / f"{outname}.json"
    with open(save_path, "w") as outfile:
        json.dump(cord_data, outfile)

    return Path(save_path)
