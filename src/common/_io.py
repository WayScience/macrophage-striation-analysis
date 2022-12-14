"""
module: _io.py

Module that contains functions responsible for moving, creating, writing and
deleting files in the current directory.
"""
import json
from pathlib import Path
from typing import List, Optional

from PIL import Image

from src.common.errors import NotCoordArrayError
from src.guards.arrays_guards import is_array_of_coords
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
        loaded_images.append(tiff_img)

    return loaded_images


def coord_to_json(
    coord_array: List[ImageCropSelection],
    outname: Optional[str] = "coord_chart",
) -> None:
    """
    Converts an array of `ImageCropSelection` and writes it out into a json
    file.

    Generated outputs will be written in the `./results` directory

    Parameters
    ----------
    coord_array : List[ImageCropSelection]
        Array of ImageCropSelection Ojects
    outname : Optional[str], optional
        name of output file generated, by default "coord_chart"
    """

    # type checking
    if not is_array_of_coords(coord_array):
        raise NotCoordArrayError(
            "'coord_array' must contains ImageCropSelection objects"
        )
    if not isinstance(outname, str):
        _type = type(outname)
        raise TypeError(f"`outname` must be a string type, not {_type}")


def json_to_coords(fpath: str | Path) -> List[ImageCropSelection]:
    """converts Json file containing coordinate data into ImageCropSelection
    data objects.

    Parameters
    ----------
    fpath : str | Path
        path to json file containing coordinate data

    Returns
    -------
    List[ImageCropSelection]
        array of coordinates that represents a selection of a specific image
    """
    # convert str to Path type
    if not isinstance(fpath, (str, Path)):
        _type = type(fpath)
        raise TypeError(f"'fpath' must be str or Path type not {_type}")

    if isinstance(fpath, str):
        fpath = Path(fpath)

    # opening json file
    raw_coord_data = json.load(fpath)
