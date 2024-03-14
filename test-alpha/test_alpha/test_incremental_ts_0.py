import time
from math import floor

import numpy as np

from .import_deps import *  # import dependencies


class AlphaIncrementalTs0(AlphaBase):
    """
    Alpha class
    """

    def set_default_params(self):
        self.run = 0

    def __init__(self,
                 universe,
                 datasets_exchange_symbols=None,
                 obj_id=(0,),
                 params=None):
        super().__init__(
            universe=universe,
            datasets_exchange_symbols=datasets_exchange_symbols,
            obj_id=obj_id,
            params=params)

        self.info('Construction starts')

        self.info('Construction completed')

    def generate(self, untrust_count=0, **inputs):
        if self.run == 0:
            while floor(time.time()) % 2 == 1:
                time.sleep(0.1)
        self.run += 1
        self.assert_inputs_length(0, **inputs)
        return np.full((1, len(self.universe)), self.run)
