import numpy as np

from .import_deps import *  # import dependencies


class AlphaTestPvCs0(AlphaBase):
    def set_default_params(self):
        self._param_diff_lookback = 12 * 24
        # alpha smooth ewm
        self._param_smooth_halflife = 12

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
        def a1():
            close_nom = np.log(close)
            close_diff = TsChange(lookback=288, method="diff")(close_nom)
            sig = (np.nanmean(close_diff) - close_diff) * 0.01
            sig = TsEwm(halflife=12)(sig)
            return sig
        """

        self.assert_checkpoint_consistency()
        self.assert_inputs_length(1, **inputs)

        close = inputs['close']
        close_log = np.log(close)
        close_diff = self.sub_op(
            contek_op_lib.TsChange,
            params={'lookback': self._param_diff_lookback, 'method': "diff"}
        )(untrust_count, input0=close_log)
        sig = (np.nanmean(close_diff) - close_diff) * 0.01
        sig = self.sub_op(
            contek_op_lib.TsEwm,
            params={'halflife': self._param_smooth_halflife}
        )(
            untrust_count,
            input0=sig
        )
        sig[np.isnan(sig)] = 0.
        return sig
