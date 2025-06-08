import pandas as pd

def add_technical_indicators(df):
    df['MA_20'] = df['Close'].rolling(window=20).mean()
    df['RSI'] = compute_rsi(df['Close'], 14)
    df['MACD'] = df['Close'].ewm(span=12).mean() - df['Close'].ewm(span=26).mean()
    return df.dropna()

def compute_rsi(series, period):
    delta = series.diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
