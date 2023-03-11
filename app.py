import smtplib
import ssl
import sqlite3
import math
import random

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server
email = "201501049@rajalakshmi.edu.in"

def OTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

    # global otp
    

    # Connect to the database
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
    subject = f"Welcome to Printconnect !"
    message = f"{otp}.\nPlease do not share it with anyone."
        # Create context
    simple_email_context = ssl.create_default_context()
    
# Connect to the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, decrypted)
    print("Connected to server :-)")

    # Send the actual email
    print()
    print(f"Sending email to - {email}")
    TIE_server.sendmail(email_from, email, f"Subject: {subject}\n\n{message}")
    print(f"Email successfully sent to - {email}")

         # If there's an error, print it out

except Exception as e:
    print(e)
