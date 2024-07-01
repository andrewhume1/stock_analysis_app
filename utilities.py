from datetime import datetime, timedelta
from api import Yahoo

import pandas as pd
from dataclasses import dataclass

yahoo = Yahoo()


@dataclass
class StockStats:
    ticker: str
    volatility_7d: float
    volatility_14d: float
    volatility_21d: float
    volatility_7d_status: str
    volatility_14d_status: str
    volatility_21d_status: str
    latest_price: float
    latest_volume: float
    latest_price_date: str
    max_52w: float
    max_52w_date: str


def read_item(ticker: str):
    df = pd.read_csv(f'output/{ticker}.csv')
    df['Name'] = ticker
    df = df[['Name', 'Date', 'Close']].iloc[-1]

    return df.to_dict()


def get_stock_data(ticker: str):
    download_ticker(ticker)
    df = pd.read_csv(f'output/{ticker}.csv')
    df['Name'] = ticker
    df = df.iloc[-252:]
    df['volatility_7d'] = df['Close'].pct_change().rolling(7).std() * (252 ** 0.5)
    df['volatility_14d'] = df['Close'].pct_change().rolling(14).std() * (252 ** 0.5)
    df['volatility_21d'] = df['Close'].pct_change().rolling(21).std() * (252 ** 0.5)
    df['volatility_mean_7'] = df['volatility_7d'].mean()
    df['volatility_mean_14'] = df['volatility_14d'].mean()
    df['volatility_mean_21'] = df['volatility_21d'].mean()

    status_7d = 'ABOVE AVERAGE' if df.iloc[-1]['volatility_7d'] > df.iloc[-1][
        'volatility_mean_7'] else 'BELOW AVERAGE'
    status_14d = 'ABOVE AVERAGE' if df.iloc[-1]['volatility_14d'] > df.iloc[-1][
        'volatility_mean_14'] else 'BELOW AVERAGE'
    status_21d = 'ABOVE AVERAGE' if df.iloc[-1]['volatility_14d'] > df.iloc[-1][
        'volatility_mean_21'] else 'BELOW AVERAGE'

    status_a = len([a for a in (status_7d, status_14d, status_21d) if a == 'A'])

    stock_stats = StockStats(ticker=ticker,
                             volatility_7d=round(df['volatility_7d'].iloc[-1], 4),
                             volatility_14d=round(df['volatility_14d'].iloc[-1], 4),
                             volatility_21d=round(df['volatility_21d'].iloc[-1], 4),
                             volatility_7d_status=status_7d,
                             volatility_14d_status=status_14d,
                             volatility_21d_status=status_21d,
                             latest_price=df['Close'].iloc[-1],
                             latest_volume=df['Volume'].iloc[-1],
                             latest_price_date=df['Date'].iloc[-1],
                             max_52w=round(df[df['Close'] == max(df['Close'])]['Close'].values[0],4),
                             max_52w_date=df[df['Close'] == max(df['Close'])]['Date'].values[0]
                             )

    return stock_stats


def download_ticker(ticker: str):
    current_date = datetime.now().strftime('%Y%m%d')
    previous_year_delta = timedelta(days=365)
    previous_year_date = datetime.now() - previous_year_delta
    previous_year_date = previous_year_date.strftime('%Y%m%d')
    yahoo.make_request(ticker=ticker, period_start=previous_year_date, period_end=current_date)
    return {"STATUS": "DONE"}
