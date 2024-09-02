import yfinance as yf
import pandas as pd
import numpy as np
import ta.momentum
import ta.trend
from helpers import get_tickers, remove_failed_tickers
import yfinance.shared as shared
from email_sender import send_email


get_tickers()

tickers = []


with open('tickers.txt', mode="r") as file:
    for line in file:
        tickers.append(line.rstrip())

data = pd.DataFrame(yf.download(' '.join(tickers), period="3mo"))

if len(shared._ERRORS.keys()) != 0:
    remove_failed_tickers(tickers, shared._ERRORS)


picks = []

for ticker in tickers:
    vals = data['Close'][ticker]
    if np.isnan(np.min(vals)):
        continue
    else:

        rsi = ta.momentum.RSIIndicator(vals, 14).rsi().iloc[-1]
        m = ta.trend.MACD(vals, 26, 12, 9)
        signal = m.macd_signal()
        macd = m.macd()

        signal_cur = signal.iloc[-1]
        line_cur = macd.iloc[-1]
    

        signal_prev_day = signal.iloc[-2]
        line_prev_day = macd.iloc[-2]

        if line_cur - signal_cur > 0 and line_prev_day - signal_prev_day <= 0 and rsi >= 40 and rsi <= 60:
            picks.append(f"{ticker}: https://finviz.com/quote.ashx?t={ticker}&ty=c&p=d&b=1")
            

MSG = "\n".join(picks)
send_email(MSG)

