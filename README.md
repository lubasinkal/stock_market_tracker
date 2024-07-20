# Stock Market Tracker

A simple Flask application that allows users to download historical stock data and visualize it using Plotly. Users can input stock tickers and date ranges to fetch data from Yahoo Finance, download the data as a CSV file, and visualize it on a separate page.

## Features

- Fetch historical stock data from Yahoo Finance
- Download stock data as a CSV file
- Visualize stock data using interactive Plotly charts

## Requirements

- Python 3.6 or higher
- Flask
- yfinance
- pandas
- plotly

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/lubasinkal/stock_market_tracker.git
    cd stock_market_tracker
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Flask application:

    ```bash
    flask run
    ```

    By default, the app will be available at `http://127.0.0.1:5000/`.

2. Open your browser and navigate to the application. 

3. **To fetch stock data**:
   - Enter the stock ticker symbol, start date, and end date.
   - Click "Submit" to fetch the data.

4. **To download the stock data**:
   - After fetching the data, click the "Download CSV" link to download the data as a CSV file.

5. **To visualize the stock data**:
   - After fetching the data, navigate to the `/visualize` page to see the interactive chart of the stock's closing prices.

## Project Structure
```bash
stock_market_tracker/
│
├── app.py # Main Flask application
├── requirements.txt # List of Python dependencies
├── templates/
│ ├── index.html # Home page with form for input
│ └── visualize.html # Page for visualizing stock data
└── venv/ # Virtual environment (not included in version control)
```