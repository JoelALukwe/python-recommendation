# AI-Powered Recommendation Engine

## 🚀 Features
- Collaborative filtering (SVD)
- Content-based recommendations
- Model versioning
- FastAPI endpoints

## 🛠 Tech Stack
| Technology | Purpose | Benefit |
|------------|---------|---------|
| **FastAPI** | API development | Async support, auto-docs |
| **Scikit-Surprise** | Recommendations | Specialized ML library |
| **Pandas** | Data processing | Efficient data manipulation |
| **Docker** | Containerization | Consistent environments |

## 💡 Skills Showcased
- **Machine Learning**: Matrix factorization, TF-IDF
- **API Design**: REST endpoints, versioning
- **Data Engineering**: ETL pipelines, feature engineering
- **MLOps**: Model deployment, monitoring

## 🛠 Setup
```bash
docker build -t recommender .
docker run -p 8000:8000 recommender


## 📖 Usage
```bash
curl http://localhost:8000/recommend/123
