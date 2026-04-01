from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from config import VECTOR_DB_PATH

# 全局向量存储
embeddings = OpenAIEmbeddings()
vector_store = Chroma(
    collection_name="my_knowledge",
    embedding_function=embeddings,
    persist_directory=VECTOR_DB_PATH
)

def add_documents(texts, metadatas=None):
    """添加文档到向量库"""
    vector_store.add_texts(texts, metadatas=metadatas)

def search(query, k=4):
    """搜索相似文档"""
    return vector_store.similarity_search(query, k=k)