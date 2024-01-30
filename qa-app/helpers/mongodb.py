from pymongo import MongoClient

client = MongoClient("mongodb+srv://naveenjothi040:HZWYv831ExjQH1UY@cluster0.nhsrzi6.mongodb.net/?retryWrites=true&w=majority")

DB_NAME = "langchain_db"
COLLECTION_NAME = "test"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "qa_app_index"

LANG_CHAIN_MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]

lang_chain_index_config = {
    "name": ATLAS_VECTOR_SEARCH_INDEX_NAME,
    "type": "vectorSearch",
    "fields": [
        {
            "type": "vector",
            "path": "embedding",
            "numDimensions": 1536,
            "similarity": "cosine"
        }
    ]
}