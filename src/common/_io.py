"""
module: _io.py

Module that contains functions responsible for moving, creating, writing and
deleting files in the current directory.
"""
import json
from pathlib import Path
from typing import List, Optional

from PIL import Image

from src.guards.arrays_guards import is_list_of_crop_selections
from src.structs.selections import ImageCropSelection


def load_tiff_images(
    img_dir: str | Path,
) -> List[Image.Image]:
    """Loads images from given directory. Returns a list object

    Parameters
    ----------
    img_dir : str | Path
       directory path containing image paths

    Returns
    -------
    List[PIL.TiffImagePlugin.TiffImageFile]
        List of tuples that contains the image path and the PIL image object

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
    if not img_dir.exists():
        raise FileNotFoundError(f"Unable to find: {str(img_dir)}")
    if img_dir.suffix == "tiff":
        raise TypeError(f"Image must be .tiff format not {img_dir.suffix}")

    # grab all .tiff images within given image directory
    tiff_paths = img_dir.glob("*.tiff")

    # loading images into memory
    # -- List[Tuple(path/to/image, PIL Image Object)]
    loaded_images = []
    for tiff_path in tiff_paths:
        tiff_img = Image.open(tiff_path)
        yield tiff_img


def coord_to_json(
    coord_array: List[ImageCropSelection],
    outname: Optional[str] = "image_cords",
):
    """Writes array of `ImageCropSelection`s into a JSON file format.

    Parameters
    ----------
    coord : List[ImageCropSelection]
        Array containing `ImageCropSelection`
    outname : Optional, optional
        Path to save output, by default "./"


    Return
    ------
    Path
        Returns path object where the json file was saved
    """
    # checking if provded array is list of `ImageCropSelection`s

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
    coord_data = {}
    for grouped_imgs in coord_array:

        if not is_list_of_crop_selections(grouped_imgs):
            raise TypeError(
                "'coord_array' must be an array of 'ImageCropSelection' objects"
            )

        crop_entries_list = []
        for crop_entry in grouped_imgs:
            meta_data_dict = crop_entry.to_dict()
            crop_entries_list.append(meta_data_dict)

        file_name = str(Path(crop_entry.file_name).name)
        coord_data[file_name] = crop_entries_list

    # saving coordinates into JSON file
    save_path = Path("./") / f"{outname}.json"
    with open(save_path, "w") as outfile:
        json.dump(coord_data, outfile)

    return Path(save_path)
