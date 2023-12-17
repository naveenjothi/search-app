from pymongo import MongoClient
import requests

client = MongoClient("mongodb+srv://naveenjothi040:YkcqV6pFILK49jGd@cluster0.nhsrzi6.mongodb.net/?retryWrites=true&w=majority")

db = client["sample_mflix"]
collection = db["movies"]

embedding_url="https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

def generateTokens(text:str)->list[float]:
    request = requests.post(embedding_url,
    headers={"Authorization":f"Bearer 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"},
    json={'inputs':text})

    if request.status_code != 200:
        raise ValueError(f"Request failed with status code {request.status_code}: {request.text}")
    return request.json()

items = collection.find({
    "plot":{"$exists":True},
    "plot_embedding_hf":{"$exists":False}
})

count = 0

for (doc) in items:
    doc["plot_embedding_hf"] = generateTokens(doc["plot"])
    print(f"Replacing {doc['title']} {count}")
    collection.replace_one({"_id":doc["_id"]},doc)
    count = count + 1

# items = collection.find().limit(5)

# for item in items:
#     print(item)