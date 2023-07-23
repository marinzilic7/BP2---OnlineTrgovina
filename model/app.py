from __init__ import session
from proizvod import Proizvod
from kategorija import Kategorija

import os 
from flask import Flask,render_template, request,redirect, url_for,flash



app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))
app.secret_key = 'ovo-je-moj-tajni-kljuc'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def index ():
    proizvod = session.query(Proizvod).all()
    kategorije = session.query(Kategorija).all()  
    return render_template('home.html', proizvod=proizvod,kategorije=kategorije)



@app.route('/dodaj-proizvod', methods=['POST'])
def dodaj_proizvod():
    naziv = request.form.get('naziv')
    opis = request.form.get('opis')
    kategorija_id = request.form.get("kategorija_id")
    cijena = request.form.get('cijena')
 
    
    
    novi_proizvod = Proizvod(naziv=naziv, ID_kategorija=kategorija_id, opis=opis, cijena=cijena)
    session.add(novi_proizvod)
    session.commit()

    return redirect(url_for('index'))


@app.route('/izbrisi_proizvod/<int:ID_proizvoda>', methods=['POST'])
def izbrisi_proizvod(ID_proizvoda):
    proizvod = session.query(Proizvod).get(ID_proizvoda)
    
    if proizvod:
        
        session.delete(proizvod)
        session.commit()  
        flash('Proizvod je uspjesno izbrisan.', 'success')

    return redirect(url_for('index'))


@app.route('/uredi_proizvod/<int:ID_proizvoda>')
def uredi_proizvod(ID_proizvoda):
    proizvod = session.query(Proizvod).get(ID_proizvoda)
    kategorije = session.query(Kategorija).all()
    return render_template('uredi_proizvod.html', proizvod=proizvod, kategorije=kategorije)


@app.route('/update_proizvod/<int:ID_proizvoda>', methods=['POST'])
def azuriraj_jelo(ID_proizvoda):
    proizvod = session.query(Proizvod).get(ID_proizvoda)
    if proizvod:
        
        proizvod.kategorija_id = request.form.get('kategorija_id')
        proizvod.naziv = request.form.get('naziv')
        proizvod.opis = request.form.get('opis')
        
        proizvod.cijena = request.form.get('cijena')
        session.commit()
        
    
       

    return redirect(url_for('index'))


app.debug = True

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000)