import numpy as np

from .import_deps import *  # import dependencies


class AlphaTestPvTs0(AlphaBase):
    def set_default_params(self):
        self._param_normalize_lookback = 12 * 24 * 7
        # alpha smooth ewm
        self._param_smooth_halflife = 12 * 8

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
        """
        def a0():
            sig = TsScaleToBook(lookback=288 * 7)(TsEwmRsi()(close[[CS("ETHUSD")]]))
            sig = TsEwm(halflife=96)(sig)
            return sig
        """

        self.assert_checkpoint_consistency()
        self.assert_inputs_length(1, **inputs)

        close = inputs['close']
        sig = self.sub_op(
            contek_op_lib.TsScaleToBook,
            params={'lookback': self._param_normalize_lookback}
        )(
            untrust_count,
            input0=self.sub_op(contek_op_lib.TsEwmRsi)(untrust_count, input0=close)
        )
        sig = self.sub_op(
            contek_op_lib.TsEwm,
            params={'halflife': self._param_smooth_halflife}
        )(
            untrust_count,
            input0=sig
        )
        sig[np.isnan(sig)] = 0.
        return sig
