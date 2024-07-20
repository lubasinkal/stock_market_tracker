from flask import Flask, render_template, request,Response
import yfinance as yf
import pandas as pd

app = Flask(__name__)

# Declare stock_data globally
stock_data = None
ticker_name = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global stock_data, ticker_name
    data = None
    if request.method == 'POST':
        ticker_name = request.form['ticker']
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        if ticker_name and start_date and end_date:
            stock_data = yf.download(ticker_name, start=start_date, end=end_date)
            data = stock_data.reset_index()

    return render_template('index.html', data=data)

@app.route('/download', methods=['GET'])
def download():
    global stock_data, ticker_name
    if stock_data is not None and ticker_name is not None:
        # Convert DataFrame to CSV
        csv = stock_data.to_csv(index=True)
        
        # Create a Response object with CSV data
        return Response(
            csv,
            mimetype='text/csv',
            headers={
               'Content-Disposition': f'attachment; filename={ticker_name}_stock_data.csv'
            }
        )
    return "No data available to download.", 404

if __name__ == '__main__':
    app.run(debug=True)
