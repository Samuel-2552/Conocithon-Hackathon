from flask import Flask, request, render_template
from geopy.geocoders import Nominatim
import os


images=os.path.join('static','images')

app = Flask(__name__)
app.config['icons'] = images

logo = os.path.join(app.config['icons'], 'logo.png')
fav_icon = os.path.join(app.config['icons'], 'fav_icon.png')



@app.route('/')
def index():
    return render_template('index.html',logo=logo,fav_icon=fav_icon)

@app.route('/update-location', methods=['POST'])
def update_location():
    data = request.get_json()
    geolocator = Nominatim(user_agent="my-app-name")
    latitude = data['latitude']
    longitude = data['longitude']
    # Do something with the latitude and longitude values
    print("lattitude", latitude)
    print("Longitude", longitude)
    location = geolocator.reverse(f"{latitude}, {longitude}", zoom=18)
    out=location

    out_str = str(out)
    out_list = out_str.split(',')
    new_list = out_list[-6:]
    print(new_list)
    out = " ".join(new_list)
    return f"{out}"

# @app.route('/otp-request')
# def otp_request():
#     data= request.get_json()
#     email

if __name__ == '__main__':
    app.run(host="0.0.0.0")
