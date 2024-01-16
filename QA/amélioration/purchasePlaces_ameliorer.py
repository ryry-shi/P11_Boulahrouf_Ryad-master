import json
from flask import Flask,render_template,request,redirect,flash,url_for
import datetime

@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if (placesRequired < 0):
        flash("Vous ne pouvez pas mettre de nombre négative")
        return render_template('welcome.html', club=club, competitions=competitions)
    if (int(club["points"]) - placesRequired < 0):
        flash("Vous n'avez pas assez de points pour réservez de ticket")
        return render_template('welcome.html', club=club, competitions=competitions)
    if placesRequired > 12:
        flash("Vous ne pouvez pas réservez plus de 12 place")
        return render_template('welcome.html', club=club, competitions=competitions)
    if competition['numberOfPlaces'] == 0:
        flash('Great-booking complete!')
    if int(competition["numberOfPlaces"]) - placesRequired < 0:
        flash("Il y a pas assez de places dans la competitions")
        return render_template('welcome.html', club=club, competitions=competitions)
    club["points"] = int(club["points"]) - placesRequired
    competition["numberOfPlaces"] = int(competition["numberOfPlaces"]) - placesRequired
    return render_template('welcome.html', club=club, competitions=competitions)