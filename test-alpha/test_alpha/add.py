from .import_deps import *  # import dependencies
import numpy as np
import pandas.core.algorithms as algos


class AlphaSumTs0(AlphaBase):
    """
    Alpha class
    """

    def set_default_params(self):
        self._param_zscore_lookback = 12 * 8
        # alpha smooth ewm
        self._param_smooth_halflife = 12 * 12

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
        def pany_easy_cs_0_func(prices,
                        zscore_lookback=12*8,
                        smooth_halflife=12*12):

            signals = (prices - prices.rolling(window=zscore_lookback).mean()) / \
                prices.rolling(window=zscore_lookback).std()

            signals = signals.rank(axis=1, ascending=True)

            signals = signals.subtract(signals.mean(axis=1), axis=0)

            signals = signals.divide(signals.abs().sum(axis=1), axis=0)

            signals = signals.fillna(0).ewm(halflife=smooth_halflife).mean()

            return signals
        """

        self.assert_checkpoint_consistency()
        self.assert_inputs_length(1, **inputs)

        prices = inputs['test_0']

        alpha = (prices - self.sub_op(contek_op_lib.TsMean, params={'lookback': self._param_zscore_lookback})(
            untrust_count, input0=prices)) / \
            self.sub_op(contek_op_lib.TsStd,
                        params={'lookback': self._param_zscore_lookback})(untrust_count, input0=prices)

        alpha = algos.rank(alpha, axis=1, ascending=True)

        alpha -= np.nanmean(alpha, axis=1, keepdims=True)

        alpha /= np.nansum(np.abs(alpha), axis=1, keepdims=True)

        alpha[np.isnan(alpha)] = 0
        alpha = self.sub_op(contek_op_lib.TsEwm, params={'halflife': self._param_smooth_halflife})(
            untrust_count, input0=alpha)

        return alpha
