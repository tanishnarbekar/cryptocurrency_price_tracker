from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_price', methods=['POST'])
def get_price():
    crypto_name = request.form['crypto'].lower()  # Convert input to lowercase for consistency
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_name}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    price = data.get(crypto_name, {}).get('usd', 'Not found')  # Get the price or a default message
    return render_template('index.html', price=price, crypto=crypto_name)

if __name__ == '__main__':
    app.run(debug=True)
