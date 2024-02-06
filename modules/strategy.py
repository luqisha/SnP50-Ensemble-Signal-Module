from hurst import compute_Hc
from modules.indicators.macd import macd_signals
from modules.indicators.bollinger import bollinger_bands

def price_behaviour(data):
    return compute_Hc(data, kind='price')[0] 

def group4_ensemble_model_signals(df):

    hurst_exp = price_behaviour(df.close)

    if hurst_exp > 0.5:
        print(f"{df.index[0]} -- {df.index[-1]} -- Price behaviour is Trend Following")
    elif hurst_exp < 0.5:
        print(f"{df.index[0]} -- {df.index[-1]} -- Price behaviour is Mean Reverting")
    else:
        print(f"{df.index[0]} -- {df.index[-1]} -- Price behaviour is Random")

    macd_sigs = macd_signals(df, 12, 26, 9)
    bb_sigs = bollinger_bands(df, 20, 2, sigs=True)

    if hurst_exp > 0.5:
        signal = macd_sigs[-1]
    elif hurst_exp < 0.5:
        signal = bb_sigs[-1]
    else:
        signal = 0

    return signal

