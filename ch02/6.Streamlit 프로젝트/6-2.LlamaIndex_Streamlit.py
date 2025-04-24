import streamlit as st
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext, VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from dotenv import load_dotenv
import os

# 현재 스크립트 파일의 디렉토리를 기준으로 상대 경로 설정
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data")

# Streamlit 앱 설정
def setup_streamlit_page():
    st.set_page_config(page_title="LlamaIndex QA", page_icon="🦙")
    st.title("RAG 관련 Q&A")

# 사이드바에 OpenAI API 키 입력 필드 추가
def setup_openai_api():
    openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
    return openai_api_key

# LLM 설정
def initialize_llm_and_settings():
    llm = OpenAI(
        temperature=0.5,
        model="gpt-4o",
        max_tokens=200,
        context_window=4096,
    )
    Settings.llm = llm
    return llm

# 데이터 로드 및 인덱스 생성
def create_index():
    # 데이터 로드
    documents = SimpleDirectoryReader(DATA_DIR).load_data()

    # 벡터 DB 생성 및 저장
    db = chromadb.PersistentClient(path="../data/chroma_db")
    chroma_collection = db.get_or_create_collection("quickstart")

    # ChromaDB를 LlamaIndex의 인덱싱 및 검색 파이프라인에 통합
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # 문서 내용을 벡터 DB에 저장
    return VectorStoreIndex.from_documents(documents, storage_context=storage_context)

def initialize_index():
    with st.spinner("Creating index..."):
        llm = initialize_llm_and_settings()
        index = create_index()
    st.success("Index created successfully!")
    return index

def process_query(index, query):
    with st.spinner("Searching for answer..."):
        query_engine = index.as_query_engine(response_mode="compact")
        response = query_engine.query(query)
    return response


def display_response(response):
    st.subheader("Answer:")
    st.write(response.response)

def main():

    setup_streamlit_page()
    openai_api_key = setup_openai_api()

    if not openai_api_key:
        st.warning("Please enter your OpenAI API key in the sidebar.")
        return

    index = initialize_index()

    # 쿼리 입력
    query = st.text_input("Enter your question:")

    if query:
        response = process_query(index, query)
        display_response(response)

if __name__ == "__main__":
    main()
