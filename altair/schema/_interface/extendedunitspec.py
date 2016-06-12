# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from .unitspec import UnitSpec
from .config import Config
from .data import Data
from .encoding import Encoding
from .mark import Mark
from .transform import Transform


class ExtendedUnitSpec(UnitSpec):
    """Wrapper for Vega-Lite ExtendedUnitSpec definition.
    
    Attributes
    ----------
    config: Config
        
    data: Data
        
    description: Unicode
        
    encoding: Encoding
        
    mark: Mark
        A name for the specification.
    name: Unicode
        
    transform: Transform
        
    """
    config = T.Instance(Config, allow_none=True, default_value=None)
    data = T.Instance(Data, allow_none=True, default_value=None)
    description = T.Unicode(allow_none=True, default_value=None)
    encoding = T.Instance(Encoding, allow_none=True, default_value=None)
    mark = Mark(allow_none=True, default_value=None, help="""A name for the specification.""")
    name = T.Unicode(allow_none=True, default_value=None)
    transform = T.Instance(Transform, allow_none=True, default_value=None)
    
    def __init__(self, config=None, data=None, description=None, encoding=None, mark=None, name=None, transform=None, **kwargs):
        kwds = dict(config=config, data=data, description=description, encoding=encoding, mark=mark, name=name, transform=transform)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(ExtendedUnitSpec, self).__init__(**kwargs)