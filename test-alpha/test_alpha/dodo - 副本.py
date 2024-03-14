from .import_deps import *  # import dependencies
import numpy as np
from contek_pyutils.contek_array import Contek2DArray

class AlphaDodo(AlphaBase):
    """
    Alpha class
    """
    _error_when_load_default_param = False
    def set_default_params(self):
        self._param_value = 0
        self._param_count = 1

    def __init__(self,
                 universe,
                 datasets_exchange_symbols=None,
                 obj_id=(0,),
                 params=None):
        super(AlphaDodo, self).__init__(
            universe=universe,
            datasets_exchange_symbols=datasets_exchange_symbols,
            obj_id=obj_id,
            params=params)
        self.info('Construction completed')

    def generate(self, untrust_count=0, **inputs):

        return Contek2DArray(
            {sym: idx for idx, sym in enumerate(self.universe)},
            np.full((self._param_count, len(self.universe)), self._param_value)
        )
