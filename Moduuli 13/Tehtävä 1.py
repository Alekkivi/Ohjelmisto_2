"""
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
"""
from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/alkuluku/<numero>')
def alkuluku(numero):
    try:
        laskuri = 0
        numero = int(numero)

        for i in range(1, numero + 1):
            if numero % i == 0:
                laskuri += 1

        if laskuri == 2:
            vastaus = {'Number': numero,
                       'isPrime': 'true'}
        else:
            vastaus = {'Number': numero,
                       'isPrime': 'false'}
        return vastaus

    except ValueError:
        tilakoodi = 400
        vastaus = {'status' : tilakoodi, 'teksti': 'Vain kokonaisluvut voi alkulukuja'}

        jsonvast = json.dumps(vastaus)
        return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
