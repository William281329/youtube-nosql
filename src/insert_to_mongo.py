# inserir no MongoDB
import json
from pymongo import MongoClient

# Conecta ao MongoDB local
client = MongoClient("mongodb://localhost:27017/")
db = client["youtube_data"]
collection = db["videos"]

# Carrega os dados do arquivo exportado
with open("../data/export.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Limpa a coleção antes (evita duplicar dados)
collection.delete_many({})

# Insere os dados
collection.insert_many(data)

print("✅ Dados inseridos com sucesso no MongoDB!")