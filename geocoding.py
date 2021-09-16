import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Base Url for geocoding
url = "https://us1.locationiq.com/v1/search.php"

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/locate', methods = ['GET', 'POST'])
def show_location():
    address = request.form['address']
    print(address)
    private_token = "pk.727f7e39de9a6cafee73b56668557864"
    data = {
        'key': private_token,
        'q': address,
        'format': 'json'
    }
    response = requests.get(url, params=data)
    latitude = response.json()[0]['lat']
    longitude = response.json()[0]['lon']
    return render_template('show.html', latitude = latitude, longitude = longitude)


if __name__ == '__main__':
    app.run(host='localhost', debug=True, port = 8000)