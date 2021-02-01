from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQlALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bookexampledbpassword@localhost/bookexample'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bookexampledbpassword@localhost:5434/bookexample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models


@app.route("/")
def home():
    return render_template('home.html',title="Home")


@app.route("/products-and-services/")
def products_and_services():
    return render_template('products-and-services.html',title="Products And Services")


@app.route("/about-us/")
def about_us():
    return render_template('about-us.html',title="About Us")

@app.route("/signup/")
def signup():
    return render_template('signup.html',title="SIGN UP", information="Use the form display to register")

@app.route("/process-signup/", methods=['POST'])
def process_signup():
 firstname = request.form['firstname']
 lastname = request.form['lastname']
 othernames = request.form['othernames']
 email = request.form['email']
 password = request.form['password']
 try:
    user = models.User(firstname=firstname, lastname=lastname, othernames=othernames, email=email, password=password)
    db.session.add(user)
    db.session.commit()

 except Exception as e:
    information = 'Could not submit.The error message is {}'.format(e.__cause__)
    return  render_template('signup.html', title="SIGN-UP", information= information)









if __name__ == "__main__":
    app.run(port=5001)



