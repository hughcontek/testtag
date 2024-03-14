from .import_deps import *  # import dependencies


class AlphaRaiseTs0(AlphaBase):
    """
    Alpha class
    """

    def set_default_params(self):
        pass

        self.info('Construction starts')

        self.info('Construction completed')

    def generate(self, untrust_count=0, **inputs):
        raise ValueError("Test throw")
