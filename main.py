from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Conexión MongoDB Atlas
MONGO_URI = "mongodb+srv://esp32:esp32pass@cluster0.uktqifs.mongodb.net/iot"

client = MongoClient(MONGO_URI)

db = client.iot
collection = db.Proyectopescera

@app.get("/")
def root():
    return {"mensaje": "API funcionando"}

@app.post("/Proyectopescera")
def guardar_sensor(data: dict):

    collection.insert_one(data)

    return {"status": "dato guardado"}
