from langchain.text_splitter import RecursiveCharacterTextSplitter

def transform_data(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    return text_splitter.split_documents(data)

