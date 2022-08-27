import pandas as pd
from yahoo_fin import stock_info as si
from short_name import *
from tqdm import tqdm


# gather stock symbols from major US exchanges
df1 = pd.DataFrame( si.tickers_sp500() )
df2 = pd.DataFrame( si.tickers_nasdaq() )
df3 = pd.DataFrame( si.tickers_dow() )
df4 = pd.DataFrame( si.tickers_other() )

# convert DataFrame to list, then to sets
sym1 = set( symbol for symbol in df1[0].values.tolist() )
sym2 = set( symbol for symbol in df2[0].values.tolist() )
sym3 = set( symbol for symbol in df3[0].values.tolist() )
sym4 = set( symbol for symbol in df4[0].values.tolist() )

# join the 4 sets into one. Because it's a set, there will be no duplicate symbols
symbols = set.union( sym1, sym2, sym3, sym4 )

# Some stocks are 5 characters. Those stocks with the suffixes listed below are not of interest.
my_list = ['W', 'R', 'P', 'Q']
del_set = set()
sav_set = set()

for symbol in tqdm(symbols):
    if len( symbol ) > 4 and symbol[-1] in my_list:
        del_set.add( symbol )
    else:
        sav_set.add( symbol )

print( f'Removed {len( del_set )} unqualified stock symbols...' )
print( f'There are {len( sav_set )} qualified stock symbols...' )

ticker_list = list(sav_set)
print(len(ticker_list))
print(ticker_list[-10:-1])

ticker_name = []
short_name = []

for i in tqdm(ticker_list[1:]):
    try:
        # print(i)
        t_name = i.strip()
        # print(f"t_name은 {t_name} 입니다.")
        s_name = get_yahoo_shortname(t_name)
        # print(f"s_name은 {s_name} 입니다.")

        short_name.append(s_name)
        ticker_name.append(t_name)
    except:
        pass

print(len(ticker_name))
print(len(short_name))

ticker_df = pd.DataFrame({'short_name': short_name})
ticker_df['ticker_name'] = ticker_name

print(ticker_df.head())  
ticker_df.to_csv("tickers.csv")  