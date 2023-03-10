from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def location():
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    # do something with the location data
    return "Received location: {}, {}".format(latitude, longitude)

if __name__ == '__main__':
    app.run()
