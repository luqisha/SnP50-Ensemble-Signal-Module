import matplotlib.pyplot as plt


def bollinger_bands(price_data, window=20, std_multiplier=2, sigs=False):
    # Load price data into a pandas DataFrame and calculate the SMA
    close_prices = price_data['close']
    ma = close_prices.rolling(window=window).mean()

    # Calculate the rolling standard deviation
    std = close_prices.rolling(window=window).std()

    # Calculate upper and lower bands
    upper_band = ma + (std_multiplier * std)
    lower_band = ma - (std_multiplier * std)

    # Generate Buy and Sell signals
    price_data['signal'] = 0  # No signal
    price_data['signal'][close_prices > upper_band] = -1  # Sell signal
    price_data['signal'][close_prices < lower_band] = 1  # Buy signal

    if sigs:
        return price_data['signal']
    else:
        return price_data['signal'], ma, upper_band, lower_band


def plot_bollinger_bands(price_data, window=20, std_multiplier=2):
    
    # Generate Bollinger Bands and Sgnals
    signals, mid_band, upper_band, lower_band = bollinger_bands(price_data, window, std_multiplier)

     # Mark the crossover points to visualize on the plot
    buy_signals = price_data[signals == 1]
    sell_signals = price_data[signals == -1]

    plt.figure(figsize=(10, 6))

    plt.plot(price_data['close'], label='Close Prices')
    plt.plot(mid_band, label='Moving Average')
    plt.plot(upper_band, label='Upper Bollinger Band')
    plt.plot(lower_band, label='Lower Bollinger Band')
    plt.scatter(buy_signals.index, buy_signals['close'], marker='^', color='g', label='Buy Signal')
    plt.scatter(sell_signals.index, sell_signals['close'], marker='v', color='r', label='Sell Signal')


    plt.title('Bollinger Bands')
    plt.xlabel('Periods')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

