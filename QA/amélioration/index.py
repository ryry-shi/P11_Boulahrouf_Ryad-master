import json
from flask import Flask,render_template,request,redirect,flash,url_for
import datetime

@app.route('/')
def index():
    return render_template('index.html')