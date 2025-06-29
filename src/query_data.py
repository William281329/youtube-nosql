# consultar dados
from pymongo import MongoClient

# Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["youtube_data"]
collection = db["videos"]

# Listar todos os vídeos
print("📺 Vídeos encontrados:")
for doc in collection.find({}, {"title": 1, "_id": 0}):
    print(f"- {doc['title']}")

# Contar comentários por vídeo
print("\n💬 Quantidade de comentários por vídeo:")
for doc in collection.find():
    title = doc['title']
    num_comments = len(doc.get("comments", []))
    print(f"- {title}: {num_comments} comentário(s)")

# (opcional) Verifica se existe a palavra "ciência" nas transcrições
print("\n🔍 Transcrições com a palavra 'ciência':")
for doc in collection.find():
    transcript_text = " ".join(doc.get("transcript", []))
    if "ciência" in transcript_text.lower():
        print(f"- {doc['title']}")