"""
This modules handle the Chroma DB Vector Store functionality.
"""

import os
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from config.config import (
    EMBEDDING_MODEL_NAME, 
    CHUNK_SIZE, CHUNK_OVERLAP
)


class AnimeVectorStore:
    def __init__(self, csv_file_path: str, persist_directory: str = "chroma_db"):
        self.csv_file_path = csv_file_path
        self.persist_directory = persist_directory
        self.embedding = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_NAME,
        )

    def create_vector_store(self) -> Chroma:
        """
        Create and persist a Chroma vector store from the CSV data.
        """

        # Load data from CSV
        loader = CSVLoader(
            file_path=self.csv_file_path, 
            encoding='utf-8',
            metadata_columns=[]
        )
        documents = loader.load()

        # Split text into smaller chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=["\n\n", "\n", " ", ""]
        )
        split_documents = text_splitter.split_documents(documents=documents)

        # Create Chroma vector store
        vector_store = Chroma.from_documents(
            documents=split_documents,
            embedding=self.embedding,
            persist_directory=self.presist_directory
        )

        # Persist the vector store to disk
        vector_store.persist()

        return vector_store
    
    def load_vector_store(self) -> Chroma:
        """ Load an existing Chroma vector store from disk."""
        # Load existing Chroma vector store from disk
        vector_store = Chroma(
            embedding_function=self.embedding,
            persist_directory=self.persist_directory
        )
        return vector_store