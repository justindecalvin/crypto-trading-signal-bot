import ccxt
import time
import pandas as pd

# Initialize the exchange (using Binance for example)
exchange = ccxt.binance()

# Function to fetch market data
def get_data(symbol, timeframe='1m', limit=100):
    bars = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    data = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
    return data

# Example function to calculate a simple moving average (SMA)
def calculate_sma(data, period=14):
    return data['close'].rolling(window=period).mean()

# Function to generate trading signals
def generate_signal(symbol):
    data = get_data(symbol)
    sma = calculate_sma(data)
    last_close = data['close'].iloc[-1]

    if last_close > sma.iloc[-1]:
        return "BUY"
    elif last_close < sma.iloc[-1]:
        return "SELL"
    else:
        return "HOLD"

# Main loop
while True:
    signal = generate_signal('BTC/USDT')
    print(f"Signal: {signal}")
    time.sleep(60)  # Sleep for 1 minute
