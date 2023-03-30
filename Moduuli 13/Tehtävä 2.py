"""
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
 Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
 Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
 Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
"""
from flask_mysqldb import MySQL
from flask import Flask, Response
import json


app = Flask(__name__)

app.config['MYSQL_HOST'] ="localhost"
app.config['MYSQL_USER'] ="user1"
app.config['MYSQL_PASSWORD'] ="sala1"
app.config['MYSQL_DB'] ="lentopeli"

mysql = MySQL(app)

@app.route('/kenttä/<ident>')
def kenttä(ident):
    try:
        sql = "SELECT ident AS ICAO, name as Name, municipality as Municipality FROM airport WHERE ident ='"+ident+"'"

        kursori = mysql.connection.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()

        if not tulos:
            raise ValueError('Kenttaa ei loydy tietokannasta')

        tilakoodi = 200
        vastaus = {
            "ICAO": tulos[0][0],
            "Name": tulos[0][1],
            "Municipality": tulos[0][2]}

        jsonvastaus = json.dumps(vastaus)
        return Response(response=jsonvastaus, status=tilakoodi, mimetype="application/json")

    except Exception as e:
            virheilmoitus = {"virhe": str(e)}
            tilakoodi = 400
            jsonvastaus = json.dumps(virheilmoitus)

            return Response(response=jsonvastaus, status=tilakoodi, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)