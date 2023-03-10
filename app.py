from flask import Flask, request, render_template
from geopy.geocoders import Nominatim
import jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update-location', methods=['POST'])
def update_location():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    # Do something with the latitude and longitude values
    return 'Location updated successfully!'

if __name__ == '__main__':
    app.run()
