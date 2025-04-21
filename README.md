# crypto-trading-signal-bot
 bot that fetches crypto market data and sends trading signals based on technical analysis.
# Crypto Trading Signal Bot

This Python bot fetches crypto market data and sends trading signals based on technical analysis.

## Features:
- Fetches real-time market data using the Binance API (you can change the exchange as needed).
- Generates signals (BUY, SELL, HOLD) based on simple moving average (SMA) crossover.
- Runs continuously with adjustable sleep intervals.

## Setup and Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/justindecalvin/crypto-trading-signal-bot.git
   python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
python -m venv venv
pip install ccxt pandas ta-lib
python bot.py
