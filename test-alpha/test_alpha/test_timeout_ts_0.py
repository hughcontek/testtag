import time

from test_alpha import AlphaSumTs0

from .import_deps import *  # import dependencies


class AlphaTimeoutTs0(AlphaSumTs0):
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
        time.sleep(5)
        return AlphaSumTs0.generate(self, untrust_count, **inputs)
