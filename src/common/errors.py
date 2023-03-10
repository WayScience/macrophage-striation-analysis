"""
module: errors.py

Module contains custom made errors specific to this module
"""


class NotCoordArrayError(TypeError):
    """Raised if the expected coord object is not a coord object"""

class ConfigAttributeNotFound(ValueError):
    """Raised if attempting to access config attribute that does not exists"""
