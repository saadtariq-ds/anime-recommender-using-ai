""" Anime recommendation pipeline loading vector store and providing recommendation. """

from src.vector_store import AnimeVectorStore
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, LLM_MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_directory: str = "chroma_db"):
        try:
            logger.info("Initializing Recommendation Pipeline...")

            vector_store = AnimeVectorStore(
                csv_file_path="",
                persist_directory=persist_directory
            )
            retriever = vector_store.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(
                retriever=retriever,
                api_key=GROQ_API_KEY,
                model_name=LLM_MODEL_NAME
            )

            logger.info("Recommendation Pipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing Recommendation Pipeline. {str(e)}")
            raise CustomException(f"Error initializing Recommendation Pipeline {str(e)}")
        
    def recommend(self, query: str) -> str:
        try:
            logger.info(f"Getting recommendations for query: {query}")
            recommendations = self.recommender.get_recommendations(query=query)
            logger.info("Recommendations retrieved successfully.")
            return recommendations
        except Exception as e:
            logger.error(f"Error getting recommendations. {str(e)}")
            raise CustomException(f"Error getting recommendations {str(e)}")