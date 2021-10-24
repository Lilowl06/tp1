from flask import Flask, render_template, request
import mysql.connector 
import os

# connection au serveur mysql
datab = mysql.connector.connect(
  host='db',
  port=3306,
  user="root",
  password="root",
  database="app"
)

app = Flask(__name__)

cursor = datab.cursor()

@app.route("/")
def home():
    return render_template("accueil.html")

@app.route("/depot")
def depotCitation():
    citation = request.args.get('citation')
    auteur = request.args.get('auteur')
    if len(request.args) == 0 :
        return render_template("formulaire.html")
    elif (citation == ''):
        return ("La saisie est incorrecte, il manque la citation")
    elif (auteur == '') :
        return ("La saisie est incorrecte, il manque l'auteur")
    else :
        cursor.execute(f"insert into recueilCitations (citation, auteur) values ('{citation}','{auteur}');")
        datab.commit()
        return (f"La citation : {citation} de {auteur} a été enregistrée !")

@app.route("/depot/<citation>/<auteur>")
def citation(citation, auteur):
    return (f"La citation est : {citation} de {auteur}")

@app.route("/citations")
def listeCitations():
    cursor.execute("select * from recueilCitations")
    citation = cursor.fetchall() # convertit le retour/resultat sql en structure
    return render_template("listeCitations.html", citation=citation)

app.run(host="0.0.0.0")