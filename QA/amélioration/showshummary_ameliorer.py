import json
from flask import Flask,render_template,request,redirect,flash,url_for
import datetime

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club,competitions=competitions)
    except IndexError:
        flash("Désolé, cet e-mail n'a pas été trouvé")
        return render_template('index.html')