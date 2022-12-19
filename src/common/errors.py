"""
module: errors.py

Module contains custom made errors specific to this module
"""


class NotCoordArrayError(TypeError):
    """Raised if the expected coord object is not a coord object"""
