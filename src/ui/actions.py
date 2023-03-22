"""
Module: actions.py

actions.py stores all the functional actions that the UI will trigger when a
user interacts with the interface.
"""
from src.common.errors import ConfigAttributeNotFound


def update_image_classification(
    crop_image_metadata: dict, classification_label: bool
) -> None:
    """Updates classification attribute with the cropped image metadata found
    within the cropped image metadata.

    The function targets the `classification` attribute within the cropped
    meta data and places a 0 or 1 as its value.

    True or False booleans are converted to 1 or 0 integers, respectively

    Parameters
    ----------
    crop_image_metadata : dict
        cropped image metadata

    classification_label : bool
        Update classification label to true or false indicating presence of
        a specific

    Returns
    -------
    None
        Updated cropped metadata under the classification attribute.
    """

    # type checking
    if not isinstance(crop_image_metadata, dict):
        input_type = type(crop_image_metadata)
        raise TypeError(
            f"cropped image data must be in dict format. not: {input_type}"
        )

    if not isinstance(classification_label, bool):
        input_type = type(classification_label)
        raise TypeError(
            f"value_update must be either True or False, not {input_type}"
        )

    # updating classification attribute
    try:
        crop_image_metadata["classification"] = int(classification_label)
    except KeyError as e:
        raise ConfigAttributeNotFound(
            "classification attributes does not exist"
        ) from e
