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

query = "imaginary characters from out space at war"

result = collection.aggregate([{
    "$vectorSearch":{
        "queryVector":generateTokens(query),
        "limit":4,
        "numCandidates":100,
        "index":"PlotSemanticSearch2",
        "path":"plot_embedding_hf"
    }
}])


for doc in result:
    print(f"Movie Name: {doc['title']},\nMovie Plot: {doc['plot']}\n")