from flask import Flask, render_template
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.foreignexchange import ForeignExchange

import matplotlib.pyplot as plt
from pprint import pprint

QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&apikey={KEY}&symbol={SYMBOL}"
API_KEY = "571I2OGDRCSK2904"

# # Time series
# ts = TimeSeries(key=API_KEY, output_format='pandas')
# data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
# data['4. close'].plot()
# plt.title('Intraday Times Series for the MSFT stock (1 min)')
# # plt.savefig('templates/my_plot.png')
# plt.show()

# # Technical Indicators
# ti = TechIndicators(key=API_KEY, output_format='pandas')
# data2, meta_data2 = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
# data2.plot()
# plt.title('BBbands indicator for  MSFT stock (60 min)')
# plt.show()
#
# # Sector Performance
# sp = SectorPerformances(key=API_KEY, output_format='pandas')
# data3, meta_data3 = sp.get_sector()
# data3['Rank A: Real-Time Performance'].plot(kind='bar')
# plt.title('Real Time Performance (%) per Sector')
# plt.tight_layout()
# plt.grid()
# plt.show()

# # Crypto Currencies
# cc = CryptoCurrencies(key=API_KEY, output_format='pandas')
# data4, meta_data4 = cc.get_digital_currency_intraday(symbol='BTC', market='CNY')
# data4['1b. price (USD)'].plot()
# plt.tight_layout()
# plt.title('Intraday value for bitcoin (BTC)')
# plt.grid()
# plt.show()

# # Foreign Exchange
# cc = ForeignExchange(key=API_KEY)
# # There is no metadata in this call
# data5, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
# pprint(data5)


#data ouput
# pprint(meta_data)
# pprint(data)



#-----------------------------------
# #Flask rendering template for HTML
#
# app = Flask(__name__)
#
# @app.route('/')
# def _request():
#     ts = TimeSeries(key=API_KEY, output_format='JSON')
#     data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
#
#     return render_template('index.html', data=data)
#
# if __name__ == '__main__':
#         app.run(debug=True)
#
