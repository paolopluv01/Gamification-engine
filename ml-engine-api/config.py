"""
Gestione centralizzata dei percorsi del progetto.
Fornisce percorsi assoluti indipendenti dalla directory di esecuzione.
"""
import os
from pathlib import Path

# Root directory del progetto
PROJECT_ROOT = Path(__file__).parent.parent #

# Directory dati
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = DATA_DIR / "models"
FEATURES_DIR = DATA_DIR / "features"
PROCESSED_DIR = DATA_DIR / "processed"
RAW_DIR = DATA_DIR / "raw"

# File modelli ML
CHURN_MODEL_PATH = MODELS_DIR / "churn_prediction_model.joblib"
FEATURE_NAMES_PATH = FEATURES_DIR / "feature_names.joblib"