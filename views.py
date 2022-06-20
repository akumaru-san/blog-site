from app import app
from models import Blog
from flask import render_template

@app.get('/')
def home():
    return({"message": "Hello World!"})

@app.get('/new/')
def new_post():
    return render_template('create.html')