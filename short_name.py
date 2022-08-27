import yfinance as fn
import urllib
import json


def get_yahoo_shortname(symbol):
    response = urllib.request.urlopen(f'https://query2.finance.yahoo.com/v1/finance/search?q={symbol}')
    content = response.read()
    data = json.loads(content.decode('utf8'))['quotes'][0]['shortname']
    return data


if __name__ == "__main__":
    print(get_yahoo_shortname("042670.KS"))