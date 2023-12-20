from langchain.document_loaders import HuggingFaceDatasetLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores.mongodb_atlas import MongoDBAtlasVectorSearch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from transformers import AutoTokenizer, pipeline
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transform_data import transform_data
from helpers.hugging_face import embeddings
from helpers.mongodb import LANG_CHAIN_MONGODB_COLLECTION,ATLAS_VECTOR_SEARCH_INDEX_NAME


dataset_name = "databricks/databricks-dolly-15k"
page_content_column = "context"

loader = HuggingFaceDatasetLoader(dataset_name,page_content_column)
data = loader.load()

docs = transform_data(data)

# insert the documents in MongoDB Atlas with their embedding
vector_search = MongoDBAtlasVectorSearch.from_documents(
    documents=docs,
    embedding=embeddings,
    collection=LANG_CHAIN_MONGODB_COLLECTION,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
)

question = "What is cheesemaking?"
searchDocs = vector_search.similarity_search(question)

print(searchDocs[0].page_content)
