from langchain.vectorstores import Chroma

def create_vector_store(documents, embeddings):
    vector_db = Chroma.from_documents(
        documents,
        embeddings
    )

    return vector_db
