from flask import Flask, render_template
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt


QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&apikey={KEY}&symbol={SYMBOL}"
API_KEY = "571I2OGDRCSK2904"

app = Flask(__name__)

@app.route('/')
def _request():
    ts = TimeSeries(key=API_KEY, output_format='JSON')
    data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')

    #Pandas Plots
    # data['4. close'].plot()
    # plt.title('Intraday Times Series for the MSFT stock (1 min)')
    # plt.savefig('templates/my_plot.png')
    # plt.show()


    return render_template('index.html', data=data)


if __name__ == '__main__':
        app.run(debug=True)




