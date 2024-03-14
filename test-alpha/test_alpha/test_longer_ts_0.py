# returns a longer position than input, to test alpha align
import numpy as np
from contek_pyutils.contek_array import Contek2DArray

from test_alpha import AlphaSumTs0

from .import_deps import *  # import dependencies


class AlphaLongerTs0(AlphaSumTs0):
    """
    Alpha class
    """

    def __init__(self,
                 universe,
                 datasets_exchange_symbols=None,
                 obj_id=(0,),
                 params=None):
        AlphaSumTs0.__init__(
            self,
            universe=universe,
            datasets_exchange_symbols=datasets_exchange_symbols,
            obj_id=obj_id,
            params=params)

        self.run = 0

    def generate(self, untrust_count=0, **inputs):
        return Contek2DArray(columns=['BTCUSD', 'ETHUSD'],
                             a=np.concatenate([np.zeros((3, 2)), AlphaSumTs0.generate(self, untrust_count, **inputs)]))


