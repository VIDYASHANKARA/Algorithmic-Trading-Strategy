# Moving Average Crossover Trading Strategy

This project implements a simple **moving average crossover trading strategy** using Python.  
The script fetches historical stock data from Yahoo Finance, computes short term and long term moving averages, and generates **buy or sell signals** based on crossover points. A visualization of the stock price, moving averages, and signals is plotted using Matplotlib.

---

## Features
- Fetches 3 years of stock data using the `yfinance` library.
- Calculates **30-day** and **100-day** Simple Moving Averages (SMA).
- Generates **buy signals** when the short-term SMA crosses above the long-term SMA.
- Generates **sell signals** when the short-term SMA crosses below the long-term SMA.
- Visualizes stock price, moving averages, and trading signals.

---
<img width="1639" height="811" alt="image" src="https://github.com/user-attachments/assets/a79842e6-6327-4717-8d2c-9ed91411bbb6" />

---
## Requirements
Install the necessary Python libraries:

```bash
pip install yfinance matplotlib
