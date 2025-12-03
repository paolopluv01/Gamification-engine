from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import numpy as np
import uvicorn
from config import CHURN_MODEL_PATH, FEATURE_NAMES_PATH

# --- 1. Caricamento Modello e Feature Names ---
try:
    # Carica il modello addestrato (Random Forest)
    model = joblib.load(CHURN_MODEL_PATH)
    # Carica l'ordine e i nomi delle feature
    feature_names = joblib.load(FEATURE_NAMES_PATH)
except FileNotFoundError:
    print("ERRORE: Assicurati che 'churn_prediction_model.joblib' e 'feature_names.joblib' siano presenti.")
    exit()

app = FastAPI(
    title="ML Churn Prediction Engine",
    description="Espone il modello di previsione Churn per l'Engine di Gamification.",
    version="1.0.0"
)

# --- 2. Definizione dello Schema di Input (Pydantic) ---

# Definisce la struttura ESATTA dei dati che il modello si aspetta.
# I valori 'Field' forniscono descrizioni utili per la documentazione automatica.

class UserFeatures(BaseModel):
    Recency: int = Field(..., description="Giorni dall'ultimo accesso (Recency, feature più importante).", ge=0, le=90)
    Frequency: int = Field(..., description="Numero totale di accessi in 90 giorni.", ge=0)
    Punti_Totali: int = Field(..., description="Punti totali accumulati dall'utente.", ge=0)
    Engagement_Rate: float = Field(..., description="Tasso di completamento dei Task (0.0 a 1.0).", ge=0.0, le=1.0)
    Volatilita_Punti_Std: float = Field(..., description="Deviazione standard dei punti ottenuti (Volatilità comportamentale).", ge=0.0)
    Task_Completati: int = Field(..., description="Numero totale di Task completati.", ge=0)

# --- 3. Endpoint di Previsione ---

@app.post("/predict_churn", response_model=dict)
def predict(features: UserFeatures):
    """
    Riceve le feature comportamentali dell'utente e restituisce la probabilità di Churn.
    Questo endpoint sarà interrogato dal microservizio Spring Boot.
    """
    
    # 1. Converte l'oggetto Pydantic in un DataFrame Pandas
    data_df = pd.DataFrame([features.model_dump()])
    
    # 2. Riordina le colonne per corrispondere all'ordine del modello addestrato
    data_df = data_df[feature_names]
    
    # 3. Effettua la previsione della probabilità di churn (classe 1)
    try:
        churn_proba = model.predict_proba(data_df)[0][1]
    except Exception as e:
        return {"error": f"Errore durante la previsione: {e}"}

    # 4. Restituisce il risultato
    return {
        "churn_probability": round(float(churn_proba), 4),
        "risk_level": "High" if churn_proba >= 0.6 else ("Medium" if churn_proba >= 0.3 else "Low")
    }

# --- 4. Avvio del Server ---

if __name__ == "__main__":
    # Esegue su http://127.0.0.1:8000
    uvicorn.run(app, host="0.0.0.0", port=8000)