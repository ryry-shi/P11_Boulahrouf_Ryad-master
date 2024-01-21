
@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)

    ##Divers bug aucunes restriction pour ne pas mettre de nombre négatif
    ##Ou ne pas mettre un nombre dans le formulaire supérieur au nombre de place que possède l'utilisateur
    ##Ou prendre plus de place que possède qu'il y en a dans la compétition