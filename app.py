from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        ticker = request.form['ticker']
        stock = yf.Ticker(ticker)
        data = stock.history(period="1mo")  # Fetch 1 month of data
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
