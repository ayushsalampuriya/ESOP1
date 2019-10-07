from flask import Flask, render_template, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/esop'
db = SQLAlchemy(app)


class Contacts(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(20), nullable=False, primary_key=True)


class Login(db.Model):
    email = db.Column(db.String(20), nullable=False, primary_key=True)
    password = db.Column(db.String(20), nullable=True)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/categories")
def categories():
    return render_template('categories.html')


@app.route("/index.html")
def index1():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num=phone, msg=message, email=email)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        '''Add entry to the database'''
        email = request.form.get('email')
        password = request.form.get('password')
        entry = Login(email=email, password=password)
        db.session.add(entry)
        db.session.commit()
    return render_template('login.html')


app.run(debug=True)
