



@app.route('/showSummary',methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html',club=club,competitions=competitions)
## bug Lorsque on taper une mauvaise adresse email


# TODO: Add route for points display
## Manque d'environnement principal

