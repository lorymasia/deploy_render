from fastapi import FastAPI
from langdetect import detect
from textblob import TextBlob

app = FastAPI()

mylist = []

@app.get("/")
def homepage():
    return "Hello World!"

@app.get("/ciao")
def saluto(nome: str, cognome: str):
    return "ciao " + nome + cognome

@app.post("/aggiungi-utente")
def aggiungi(username: str):
    mylist.append(username)
    return "utente aggiunto"
    
@app.get("/cerca-utente")
def cerca(username: str):
    if username in mylist:
        return True
    else:
        return False
    
@app.get("/totale_utenti")
def totale():
    return len(mylist)

@app.delete("/elimina-utente")
def elimina(username: str):
    if username in mylist:
        mylist.remove(username)
        return "Eseguito"
    else:
        return "Errore"

@app.get("/capisci_lingua")
def lingua(testo):
    lingua = detect(testo)
    return (f"La lingua rilevata è: {lingua}")
    
@app.get("/sentiment_testo")
def sentiment(testo):
    blob = TextBlob(testo)
    sentiment = blob.sentiment.polarity
    
    # Se sentiment > 0 allora -> positivo
    # Se sentiment < 0 allora -> negativo
    # Se sentiment = 0 allora -> neutro
    if sentiment > 0:
        return (f"umore positivo: {float(sentiment)}")
    elif sentiment < 0:
        return (f"umore negativo: {float(sentiment)}")
    else:
        return (f"umore neutro: {float(sentiment)}")
