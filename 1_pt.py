#pip install numpy scipy scikit-learn pandas DateTime statsmodels
#https://www.youtube.com/watch?v=84zGcQkYioo

import matplotlib.pyplot as plt
import yfinance as yf
import datetime
import pandas as pd
import statsmodels.tsa.stattools as ts
from scipy.stats import linregress

def download_data(stock, start, end):
    stock_data = {}
    ticker = yf.download(stock, start, end)
    stock_data['price'] = ticker['Adj Close']
    return pd.DataFrame(stock_data)

def plot_pairs(data1, data2):
    fig, (ax1, ax2)  = plt.subplots(2)
    fig.suptitle('Pair of Stocks')
    ax1.plot(data1)
    ax2.plot(data2)
    plt.show()


def scater_plot(data1,  data2):
    plt.scatter(data1.values, data2.values)
    plt.xlabel('XOM')
    plt.ylabel('CVX')
    plt.show()



if __name__  == '__main__':
    start_date = datetime.datetime(2011, 4, 1)
    end_date = datetime.datetime(2013, 1,  1)

    pair1 = download_data('XOM', start_date, end_date)
    pair2 = download_data('CVX', start_date, end_date)

    #print(pair1)
    #print(pair1.values)
    
    plot_pairs(pair1, pair2)
    scater_plot(pair1, pair2)

    #linear regression
    #print(pair1.values)
    #print(pair1.values[:, 0])

    result = linregress(pair1.values[:,  0], pair2.values[:,  0])
    print(result)

    #проверка на стационарность
    residuals = pair1 - result.slope * pair2

    adf = ts.adfuller(residuals)
    print(adf)


#3:48

