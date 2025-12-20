""" File to define the AnimeRecommender class which uses a retrieval-based QA chain to provide anime recommendations. """

from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from src.prompt_templates import get_anime_prompt



class AnimeRecommender:
    def __init__(self, retriever: Chroma, api_key: str, model_name: str):
        self.llm = ChatGroq(name=model_name, groq_api_key=api_key, temperature=0)
        self.prompt = get_anime_prompt()
        self.retriever = retriever
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )

    def get_recommendations(self, query: str) -> dict:
        """
        Get anime recommendations based on the user's query.
        """
        response = self.qa_chain.invoke({"query": query})
        return response["result"]
        