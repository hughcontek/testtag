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
                 

        self.run = 0

    def generate(self, untrust_count=0, **inputs):
        return Contek2DArray(columns=['BTCUSD', 'ETHUSD'],
                             a=np.concatenate([np.zeros((3, 2)), AlphaSumTs0.generate(self, untrust_count, **inputs)]))


