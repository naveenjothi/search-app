from langchain.document_loaders import HuggingFaceDatasetLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores.mongodb_atlas import MongoDBAtlasVectorSearch
from transformers import AutoTokenizer, pipeline
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transform_data import transform_data
from helpers.hugging_face import embeddings,generateHFEmbeddings
from helpers.mongodb import LANG_CHAIN_MONGODB_COLLECTION,ATLAS_VECTOR_SEARCH_INDEX_NAME
from helpers.qa_pipeline import qa_pipe,model_name
from langchain_core.prompt_values import PromptValue



vector_search = MongoDBAtlasVectorSearch(
    collection=LANG_CHAIN_MONGODB_COLLECTION,
    embedding=embeddings,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
)

question = "Who is Thomas Jefferson?"


# question = "What is cheesemaking?"
# searchDocs = vector_search.similarity_search(question)
# print(searchDocs[0].page_content)

# print[result[0].page_content]

llm = HuggingFacePipeline(
    pipeline=qa_pipe,
    model_kwargs={"temperature": 0.7, "max_length": 512}
)

retriever = vector_search.as_retriever(search_kwargs={"k": 4})

qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="refine", retriever=retriever, return_source_documents=False)

# question = "Who is Thomas Jefferson?"


# result = qa_chain.run(input_data)


# print(result["result"])

# print(result)





