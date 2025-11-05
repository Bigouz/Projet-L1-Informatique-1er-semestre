import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import asyncio
from contextlib import asynccontextmanager
import sqlite3
import score as score

@asynccontextmanager # gestion du cycle de vie de l'application (onstartup/shutdown)
async def lifespan(app : FastAPI):
    # Code à exécuter au démarrage de l'application
    # Initialisation de la base de données SQLite
    connect = sqlite3.connect('singonlight.db')
    connect.execute('CREATE TABLE IF NOT EXISTS calibration (id INTEGER PRIMARY KEY AUTOINCREMENT, seuil INTEGER)') # utilisé afin d'obtenir le seuil de calibration
    connect.execute('CREATE TABLE IF NOT EXISTS scores (id INTEGER, score INTEGER, maxScore INTEGER)') # utilisé afin d'obtenir les scores des parties jouées
    everything = connect.execute('SELECT * FROM calibration')
    data = everything.fetchall()
    if len(data) == 0:
        connect.execute('INSERT INTO calibration (id,seuil) VALUES (?,?)', (1,50)) # valeur par défaut du seuil de calibration
    connect.commit()
    connect.close()
    print("Base de données initialisée.")
    yield
    # Code à exécuter à l'arrêt de l'application
    pass

#print(score.calculer([1,0,1,1,0,0,1],[0,1,1,1,0,0,1])) # Test de la fonction de calcul du score

templates = Jinja2Templates(directory="templates/")
app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get('/')
def main(request:Request):
    #user = {'username': 'Cécile'}
    return templates.TemplateResponse("index.html",{"request":request})

@app.get("/play.html")
def play(request:Request) -> str:
    return templates.TemplateResponse('play.html',{'request': request})

@app.get("/data.html")
def data(request:Request) -> str:
    return templates.TemplateResponse('data.html',{'request': request})

@app.get("/calibration.html")
def calibration(request:Request) -> str:
    connect = sqlite3.connect('singonlight.db')
    seuil = connect.execute('SELECT seuil FROM calibration').fetchone()[0]
    connect.close()
    return templates.TemplateResponse('calibration.html',{'request': request, 'seuil':int(seuil)})

def save_calibration(seuil: int):
    connect = sqlite3.connect('singonlight.db')
    connect.execute('UPDATE calibration set seuil=(?) WHERE id=1', (seuil,))
    connect.commit()
    connect.close()


@app.post("/run-calibrate") # récupération du seuil de calibration depuis la page calibration.html afin de le sauvegarder dans la base de donnée
async def run_calibrate(request:Request):
    body = await request.json()
    seuil = body.get("seuil", 50)
    result = save_calibration(int(seuil))
    return result

if __name__ == "__main__":
    uvicorn.run(app) # lancement du serveur HTTP + WSGI avec les options de debug


def transformer_signal_audio(signal_audio, seuil):
    """Transforme un signal audio en une liste binaire en fonction d'un seuil donné."""
    pass  # Implémentation à venir