from .import_deps import *  # import dependencies


class AlphaRadddiseTs0(AlphaBase):
    """
    Alpha class
    """

    def set_default_params(self):
        pass

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
        raise ValueError("Test throw")
