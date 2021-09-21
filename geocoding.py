'''Geocoding Flask project
This program is a flask project that allows a user to input an address
and return to the user the latitude and longitude of that address.

The script requires that requests be installed as well as flask within
the python enviroment you are running the program in.
'''
import requests
from flask import Flask, render_template, request

#test
app = Flask(__name__)

# Base Url for geocoding
URL = "https://us1.locationiq.com/v1/search.php"
# Token for api call
PRIVATE_TOKEN = "pk.727f7e39de9a6cafee73b56668557864"

def get_geo(address):
    '''
    Function that holds all of the functionality to find latitude
    and longitude
    '''
    data = {
        'key': PRIVATE_TOKEN,
        'q': address,
        'format': 'json'
    }
    response = requests.get(URL, params=data)
    latitude = response.json()[0]['lat']
    longitude = response.json()[0]['lon']
    geo_lst = [latitude, longitude]
    return geo_lst

@app.route('/')
def welcome():
    '''
    Start page with form on it
    '''
    return render_template('home.html')

@app.route('/locate', methods = ['GET', 'POST'])
def show_location():
    '''
    Page that returns the latitude and longitude of the address
    entered in
    '''
    lst = get_geo(request.form['address'])
    return render_template('show.html', latitude = lst[0], longitude = lst[1])

@app.route('/curl-test/<address>')
def show_curl_location(address):
    '''
    Dummy route used only for curl testing with bash file
    '''
    address = address.replace(' ', '-')
    lst = get_geo(request.form['address'])
    return render_template('curlshow.html', latitude = lst[0], longitude = lst[1])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
