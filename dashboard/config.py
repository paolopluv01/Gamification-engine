import os

# ----------------------------------------------------------------------
# 1. IMPOSTAZIONI DI BASE DEL PROGETTO
# ----------------------------------------------------------------------

# 1. Trova la directory di config.py (ad esempio: /progetto/sottocartella)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Risali di un livello per trovare la directory radice del progetto
#    (ad esempio: /progetto/)
BASE_DIR = os.path.dirname(CURRENT_DIR)

# ----------------------------------------------------------------------
# 2. PERCORSI DEI FILE (PATHS)
# ----------------------------------------------------------------------

# Cartella che contiene tutti i dati e i modelli
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Percorsi specifici dei file richiesti dall'applicazione
CHURN_MODEL_PATH = os.path.join(DATA_DIR, 'models/churn_prediction_model.joblib')
FEATURE_NAMES_PATH = os.path.join(DATA_DIR, 'features/feature_names.joblib')
USER_FEATURES_PATH = os.path.join(DATA_DIR, 'processed/user_features_ml_ready.csv')
USERS_BASE_PATH = os.path.join(DATA_DIR, 'raw/gamification_users_base.csv') # Aggiunto per Bokeh
'''
# ----------------------------------------------------------------------
# 3. IMPOSTAZIONI DEL MODELLO
# ----------------------------------------------------------------------

# Soglie di rischio per l'interpretazione dei risultati (usate in app.py)
RISK_THRESHOLDS = {
    'ALTO': 0.70,     # Probabilità >= 70%
    'MODERATO': 0.40, # Probabilità >= 40%
    'BASSO': 0.0      # Probabilità < 40%
}

# ----------------------------------------------------------------------
# 4. IMPOSTAZIONI DELL'INTERFACCIA UTENTE (STREAMLIT/BOKEH)
# ----------------------------------------------------------------------

APP_TITLE = "🎯 Behavioral Gamification Engine: Demo Portfolio"
PAGE_CONFIG = {
    "layout": "wide",
    "page_title": "Behavioral Gamification Engine Demo"
}

# Valori di default e range per gli slider di simulazione
SLIDER_DEFAULTS = {
    'Recency': {'min': 1, 'max': 90, 'default': 30, 'step': 1},
    'Frequency': {'min': 1, 'max': 150, 'default': 50, 'step': 5},
    'Punti_Totali': {'min': 0, 'max': 30000, 'default': 5000, 'step': 500},
    'Engagement_Rate': {'min': 0.0, 'max': 1.0, 'default': 0.5, 'step': 0.05},
    'Volatilita_Punti_Std': {'min': 0, 'max': 1000, 'default': 200, 'step': 50},
    'Task_Completati': {'min': 0, 'max': 100, 'default': 25, 'step': 5}
}

# Impostazioni colori Bokeh (per coerenza visiva)
BOKEH_COLORS = {
    'CHURNED': 'red', # Corrisponde a Category10[3][0]
    'ATTIVO': 'green' # Corrisponde a Category10[3][2]
}
'''