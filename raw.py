from pymongo import MongoClient
import json
from collections import Counter as Contador

cliente = MongoClient("mongodb://localhost:27017")

db = cliente["onepiece"]
colecao = db["onepiece_collection"]

#with open("One Piece Json.json", "r") as arquivo:
#    dados = json.load(arquivo)

#colecao.insert_many(dados)

#for doc in colecao.find().limit(5):
#    print(doc)

total = colecao.count_documents({})
print (f"total de documentos: {total}")

campos = set()
for doc in colecao.find():
    campos.update(doc.keys())
print (f"Campos únicos encontrados\n")
print (sorted(campos))

anos = [doc["start"] for doc in colecao.find()]
contagem = Contador (anos)
for ano, qtd in sorted(contagem.items()): 
    print (f"{ano}: {qtd}")