from flask import Flask, request, render_template
from geopy.geocoders import Nominatim
import os
import smtplib
import ssl
import sqlite3
import math
import random

smtp_port = 587
smtp_server = "smtp.gmail.com"
images=os.path.join('static','images')
otp=""
app = Flask(__name__)
app.config['icons'] = images

logo = os.path.join(app.config['icons'], 'logo.png')
fav_icon = os.path.join(app.config['icons'], 'fav_icon.png')

latitude = None
longitude = None


@app.route('/')
def index():
    return render_template('index.html',logo=logo,fav_icon=fav_icon)

@app.route('/shopkeeper')
def shopkeeper():
    return render_template('shopkeeper.html',logo=logo,fav_icon=fav_icon)

@app.route('/update-location', methods=['POST'])
def update_location():
    global latitude,longitude
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

def OTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

@app.route('/otp', methods=['POST'])
def otpt():
    global otp
    # global simple_email_context
    data = request.get_json()
    email = data['email']
    conn_cred = sqlite3.connect('cred.db')

    # Create a cursor
    cursor_cred = conn_cred.cursor()

        # Execute an SQL command to retrieve the first row from the user table
    cursor_cred.execute('SELECT * FROM user LIMIT 1')

        # Fetch the first row and print it
    row = cursor_cred.fetchone()
    email_from=row[1]
    decrypted=row[2]

        # Close the connection
    conn_cred.close()
    try:
        otp = OTP() + " is your OTP"
        subject = f"Welcome th Printconnect !"
        message = f"{otp}.\nPlease do not share it with anyone."
        simple_email_context = ssl.create_default_context()
        print("Connecting to server...")
        tie_server = smtplib.SMTP(smtp_server,smtp_port)
        tie_server.starttls(context=simple_email_context)
        tie_server.login(email_from, decrypted)
        print()
        print(f"Sending email to - {email}")
        tie_server.sendmail(email_from, email, f"Subject: {subject}\n\n{message}")
        print(f"Email successfully sent to - {email}")
        return "success"
    except Exception as e:
        print(e)
        return "failure"
    
@app.route('/otp1', methods=['POST'])
def otp1():
    global otp
    # global simple_email_context
    data = request.get_json()
    otp_1 = data['otp']
    otp_1 = str(otp_1) +" is your OTP"
    print(otp_1)
    if (otp1==otp):
        return "Success"
    else:
        return "Failure"




@app.route("/shop_login", methods=['GET','POST'])
def shop_login():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        pname = request.form['pname']
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        
        # cur.execute("INSERT INTO user (username, email, latitude, longitude, printername) VALUES (?, ?, ?)", (name,email,latitude,longitude,pname))
        cur.execute("SELECT email from user where email=(?)",(email,))
        data = cur.fetchone()
        print(data)
        if(data):
            return render_template("shopkeeper.html",logo=logo,fav_icon=fav_icon)
        else:
            cur.execute("INSERT INTO user (username, email, latitude, longitude, printername) VALUES (?, ?, ?,?,?)", (name,email,latitude,longitude,pname))
    return render_template("shopavailable.html", name = name, logo=logo,fav_icon=fav_icon)


    


if __name__ == '__main__':
    app.run(host="0.0.0.0")


