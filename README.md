## A python module containing an ensemble strategy built upon 50 diversified stocks fomr S&P50

### Installation
`pip install git+https://github.com/luqisha/SnP50-Ensemble-Signal-Module.git`

### Usage
```python
from ensemble_strategy.modules.strategy import group4_ensemble_model_signals

signal = group4_ensemble_model_signals(time_series_dataframe)
```

### Documentation
```python
def group4_ensemble_model_signals(df, return_stability=False):
"""
Generate trading signal of the latest day based on the price behaviour of the data.

Parameters:
    - df (pandas.DataFrame): DataFrame containing financial data, with 'date' as index 'close' as one of the columns.
    - return_stability (bool): Whether to return the stability measure along with the signal.

Returns:
    - int or tuple: Trading signal (by default) or tuple containing trading signal and stability measure (if return_stability= True).
"""
```

### Dependency
- [Hurst](https://pypi.org/project/hurst/)
- Pandas
- Matplotlib