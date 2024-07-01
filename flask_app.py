from flask import Flask, request, render_template
import utilities

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form['ticker']
        # Call an API or database to retrieve stock information
        stock_stats = utilities.get_stock_data(ticker)
        return render_template('index.html', stock_price=stock_stats.latest_price,
                               volatility_7d=stock_stats.volatility_7d,
                               status_7d=stock_stats.volatility_7d_status,
                               volatility_14d=stock_stats.volatility_14d,
                               status_14d=stock_stats.volatility_14d_status,
                               volatility_21d=stock_stats.volatility_21d,
                               status_21d=stock_stats.volatility_21d_status,
                               latest_price_date=stock_stats.latest_price_date,
                               max_52w=stock_stats.max_52w,
                               max_52w_date=stock_stats.max_52w_date,
                               latest_volume=stock_stats.latest_volume)
    else:
        return render_template('index.html')
