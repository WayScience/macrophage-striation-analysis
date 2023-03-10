"""
Module: actions.py

actions.py stores all the functional actions that the UI will trigger when a 
user interacts with the interface. 
"""
from src.common.errors import ConfigAttributeNotFound

def load_images_to_ui():
    pass

def update_image_classification(crop_image_metadata: dict, value_update: bool):
    """Updates classification attribute with the cropped image metadata.
    Classification 

    Parameters
    ----------
    crop_image_metadata : dict
        cropped image metadata 

    value_update : bool


    """

    # type checking
    if not isinstance(crop_image_metadata, dict):
        input_type = type(crop_image_metadata)
        raise TypeError(f"cropped image data must be in dict format. not: {input_type}")

    if not isinstance(value_update, bool):
        input_type = type(value_update)
        raise TypeError(f"value_update must be either True or False, not {input_type}")

    # updating classification attribute
    try:
        crop_image_metadata["classification"] = value_update
    except KeyError as e:
        raise ConfigAttributeNotFound(
            "classification attributes does not exist"
        ) from e




























# -----------------
# private functions
# -----------------