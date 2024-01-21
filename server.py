import json
from flask import Flask,render_template,request,redirect,flash,url_for
import datetime

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club,competitions=competitions)
    except IndexError:
        flash("Désolé, cet e-mail n'a pas été trouvé")
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition,club):
    try:
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
        date_passed = datetime.datetime.fromisoformat(foundCompetition["date"])
        if date_passed < datetime.datetime.today():
            flash("vous ne pouvez pas réservez une place pour un spectacle déja produit")
            return render_template('welcome.html',club=foundClub,competitions=competitions)
        if foundClub and foundCompetition:
            return render_template('booking.html',club=foundClub,competition=foundCompetition)
    except IndexError:
        return render_template("index.html"),404


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


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)

