from pathlib import Path

class Config:
  RANDOM_SEED = 90
  ASSETS_PATH = Path("../")
  REPO = "C:\\Users\\1221\\Desktop\\Acadamy AIM 2\\Pharmaceutical-Data\\data\\rossmann-store-sales_data"
  DATASET_FILE_PATH = "data/train.csv"
  DATASET_PATH = ASSETS_PATH / "data"
  FEATURES_PATH = ASSETS_PATH / "features"
 # MODELS_PATH = ASSETS_PATH / "models"