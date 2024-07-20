from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        ticker = request.form['ticker']
        stock = yf.Ticker(ticker)
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        if ticker and start_date and end_date:
            stock_data = yf.download(ticker, start=start_date, end=end_date)
            data = stock_data.reset_index()

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
