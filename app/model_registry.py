import pickle
from pathlib import Path
from surprise import SVD, Dataset

MODEL_DIR = Path("models")

class ModelRegistry:
    def __init__(self):
        MODEL_DIR.mkdir(exist_ok=True)
        
    def train_new_model(self):
        data = Dataset.load_builtin('ml-100k')
        algo = SVD()
        algo.fit(data.build_full_trainset())
        
        model_path = MODEL_DIR / "latest_model.pkl"
        with open(model_path, "wb") as f:
            pickle.dump(algo, f)
            
        return model_path
