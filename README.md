## A python module containing an ensemble strategy built upon 50 diversified stocks fomr S&P50
### Installation
`pip install -e git+https://github.com/luqisha/SnP50-Ensemble-Signal-Module.git`

### Usage
```
from ensemble_strategy.modules.strategy import group4_ensemble_model_signals

signal = group4_ensemble_model_signals(time_series_data)
```

### Documentation
def group4_ensemble_model_signals(df, return_stability=False):
    """
    Generate trading signal of the latest day based on the price behaviour of the data.

    Parameters:
    - df (pandas.DataFrame): DataFrame containing financial data, with 'date' as index 'close' as one of the columns.
    - return_stability (bool): Whether to return the stability measure along with the signal.

    Returns:
    - int or tuple: Trading signal or tuple containing trading signal and stability measure.
    """


### Dependency
- [Hurst](https://pypi.org/project/hurst/)
- Pandas
- Matplotlib




