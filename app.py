from flask import Flask, request, render_template
from geopy.geocoders import Nominatim
import jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['GET'])
def location():
    latitude = request.args.get('lat')
    longitude = request.args.get('long')
    return jsonify({'latitude': latitude, 'longitude': longitude})

if __name__ == '__main__':
    app.run()
