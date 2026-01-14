# 🎌 AI Anime Recommender

AI Anime Recommender is a **Generative AI–based recommendation system** that helps users discover anime tailored to their interests. It leverages **LLM reasoning**, **semantic embeddings**, and **vector similarity search** to provide accurate and context-aware recommendations.

The application uses **Groq LLM** for fast inference, **Hugging Face embeddings** with **ChromaDB** for vector search, a **Streamlit frontend**, and is deployed on **Kubernetes (Minikube) running inside a GCP VM**. Cluster-level monitoring is handled via **Grafana Cloud**.


## 🚀 Features

- 🤖 AI-powered anime recommendations using Groq LLM
- 🧠 Semantic understanding with Hugging Face embedding models
- 🔍 Vector-based similarity search using ChromaDB
- 🔗 LangChain for orchestration between LLM and vector store
- 🎨 Interactive Streamlit web interface
- 🐳 Dockerized application for consistent deployments
- ☸️ Kubernetes deployment using Minikube
- ☁️ Hosted on Google Cloud VM
- 📊 Kubernetes monitoring and observability with Grafana Cloud

## 🧱 System Architecture

1. User provides music preferences via Streamlit UI  
2. LangChain structures prompts for the Groq LLM  
3. LLM generates symbolic music instructions (notes, chords)  
4. Music21 validates and processes music theory elements  
5. Synthesizer converts notes into audio waveforms  
6. Docker image is built and pushed to GCP Artifact Registry  

## 🛠️ Tech Stack

| Category | Tools |
|--------|------|
| LLM | Groq |
| Embeddings | Hugging Face |
| GenAI Framework | LangChain |
| Vector Store | ChromaDB |
| Frontend | Streamlit |
| Containerization | Docker |
| Orchestration | Kubernetes (Minikube) |
| CLI | kubectl |
| Cloud | GCP VM |
| Monitoring | Grafana Cloud |
| SCM | GitHub |

# ⚙️ Local Setup
## 1️⃣ Clone the Repository
```bash
git clone https://github.com/saadtariq-ds/anime-recommender-using-ai.git
cd anime-recommender-using-ai
```

## 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

## 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 4️⃣ Run the App
```bash
streamlit run app/app.py
```

