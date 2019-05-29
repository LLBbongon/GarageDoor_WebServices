import logging
import psycopg2
from flask import Flask, render_template, request, flash, redirect, url_for
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

webpage = {'homecontrol': 'Welcome to Home Control', 'garagecontrol': 'Welcome to Garage Control'}

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        familyData_username = form.username.data
        familyData_password = form.password.data
        
        return redirect(url_for('GaragePage'))
    return render_template('HomeControl.html', title = webpage, form=form)



        
@app.route('/GaragePage', methods=['GET', 'POST'])
def GaragePage():
     
     return render_template('GarageDoor.html')
    

if __name__ == '__main__':
    app.run(debug=True, port=8079, host='192.168.1.113')
