"""
module: _io.py

Module that contains functions responsible for moving, creating, writing and
deleting files in the current directory.
"""
import json
from pathlib import Path
from typing import List, Optional

from src.common.errors import NotCoordArrayError
from src.guards.arrays_guards import is_array_of_coords
from src.structs.selections import ImageCropSelection


# TODO: must finish later
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
