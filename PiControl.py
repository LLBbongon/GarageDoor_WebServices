import logging
import psycopg2
import time
from database import Database_FetchUser, Database_FetchPassword
from flask import Flask, render_template, request, flash, redirect, url_for
from config import Config
from forms import LoginForm
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

app.config.from_object(Config)

webpage = {'homecontrol': 'Welcome to Home Control', 'garagecontrol': 'Welcome to Garage Control'}

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        
        familyData_username = form.username.data
        familyData_password = form.password.data
        
        fetch_html_username = Database_FetchUser(familyData_username)
        fetch_html_password = Database_FetchPassword(familyData_password)
        app.logger.info(fetch_html_username)
        app.logger.info(fetch_html_password)
        
        if familyData_username == fetch_html_username and fetch_html_password == True:
            return redirect(url_for('GaragePage'))
        else:
            app.logger.info("Try Again")
        
    return render_template('HomeControl.html', title = webpage, form=form)


@app.route('/GaragePage', methods=['GET', 'POST'])
def GaragePage():
    return render_template('GarageDoor.html')
    
@app.route('/<action>')
def GarageDoor(action):
    if action == "on":
        GPIO.output(21, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(21, GPIO.LOW)
    else:
        GPIO.output(21, GPIO.LOW)
    return render_template('GarageDoor.html')
    

if __name__ == '__main__':
    app.run(debug=True, port=8079, host='192.168.1.113')
