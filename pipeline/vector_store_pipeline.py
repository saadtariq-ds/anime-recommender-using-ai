""" Pipeline to create and persist vector store from anime data. """

from src.data_loader import AnimeDataLoader
from src.vector_store import AnimeVectorStore
from utils.logger import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv
load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting vector store creation process...")
        data_loader = AnimeDataLoader(
             original_csv="data/anime_with_synopsis.csv",
             processed_csv="data/processed_anime_data.csv")
        
        processed_csv = data_loader.load_and_process_data()

        logger.info("Data loaded and processed...")

        vector_store = AnimeVectorStore(
            csv_file_path=processed_csv,
            presist_directory="chroma_db"
        )
        vector_store.create_vector_store()
        logger.info("Vector store created and persisted successfully.")

    except Exception as e:
            logger.error(f"Error getting recommendations. {str(e)}")
            raise CustomException(f"Error getting recommendations {str(e)}")

if __name__=="__main__":
    main()