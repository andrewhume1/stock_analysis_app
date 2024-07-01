import requests
import datetime
import pandas as pd
import io


def convert_to_epoch(date):
    return int(datetime.datetime.strptime(date, '%Y%m%d').timestamp())


class Yahoo:
    def __init__(self):
        self.url = 'https://query1.finance.yahoo.com/v7/finance/download/'

    def make_request(self, ticker, period_start, period_end):
        url = self.url + ticker
        params = {'period1': convert_to_epoch(period_start),
                  'period2': convert_to_epoch(period_end),
                  'interval': '1d',
                  'events': 'history',
                  'includeAdjustedClose': True}
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0'}
        resp = requests.get(url=url, params=params, headers=headers)
        df = pd.read_csv(io.StringIO(resp.text))
        df['Ticker'] = ticker
        df.to_csv(f'./output/{ticker}.csv')
        return df
