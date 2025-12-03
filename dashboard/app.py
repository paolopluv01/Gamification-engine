import streamlit as st
import pandas as pd
import joblib
#import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, CategoricalColorMapper
from bokeh.palettes import Category10
from bokeh.transform import factor_cmap
from config import CHURN_MODEL_PATH, FEATURE_NAMES_PATH, USER_FEATURES_PATH, USERS_BASE_PATH

# --- 1. Caricamento Risorse ---
try:
    # Carica il modello ML e le feature list
    # - Carica il modello di Machine Learning addestrato
    model = joblib.load(CHURN_MODEL_PATH)
    feature_names = joblib.load(FEATURE_NAMES_PATH)
    df_features = pd.read_csv(USER_FEATURES_PATH)
except FileNotFoundError:
    st.error("Errore: Assicurati che 'churn_prediction_model.joblib', 'feature_names.joblib' e 'user_features_ml_ready.csv' siano presenti nella stessa directory.")
    st.stop()
except Exception as e:
    st.error(f"Errore durante il caricamento delle risorse: {e}")
    st.stop()


# --- 2. Funzioni Ausiliarie ---

def predict_churn(input_data):
    """Calcola la probabilità di Churn (abbandono) per un utente."""
    # Converti l'input in DataFrame
    input_df = pd.DataFrame([input_data])
    # Ordina le colonne per assicurarne la corrispondenza con il training set
    input_df = input_df[feature_names]

    # Previsione della probabilità (classe 1 = Churn)
    prob_churn = model.predict_proba(input_df)[:, 1][0]
    return prob_churn


def calculate_feature_importance():
    """Calcola l'importanza delle features dal modello (per la visualizzazione)."""
    # Se il modello supporta feature_importances_ (es. Random Forest)
    if hasattr(model, 'feature_importances_'):
        importances = pd.Series(
            model.feature_importances_, index=feature_names)
        return importances.sort_values(ascending=False)
    return None

# --- 3. Struttura dell'Applicazione Streamlit ---


st.set_page_config(
    layout="wide", page_title="Behavioral Gamification Engine Demo")

st.title("🎯 Behavioral Gamification Engine: Demo Portfolio")
st.markdown("Mostra l'uso del **Machine Learning** e **Data Analysis** per la **Loyalty** e la prevenzione del *Churn* in contesti di Gamification.")

st.divider()

# Layout in due colonne: analisi e simulazione
col1, col2 = st.columns([2, 1])

with col1:
    # ... (Il codice precedente per Analisi Comportamentale e Importanza delle Features)

    st.markdown("---")

    st.header("✨ Visualizzazione Interattiva (Bokeh)")
    st.subheader("Relazione tra Recency e Engagement Rate")
    st.markdown("Analisi della distribuzione degli utenti a rischio (*Churned* vs *Attivi*) in base alle due metriche comportamentali chiave.")

    # --- 3.1 Creazione del Data Source per Bokeh ---

    # Uniamo le feature ML al DataFrame originale degli utenti per includere la Categoria
    df_bokeh = df_features.merge(pd.read_csv( USERS_BASE_PATH)[
                                 ['UserID', 'Categoria']], on='UserID', how='left')

    # Convertiamo la colonna Churned in una stringa categorica per l'etichettatura
    df_bokeh['Churn_Status'] = df_bokeh['Churned'].apply(
        lambda x: 'CHURNED (Alto Rischio)' if x == 1 else 'ATTIVO (Basso Rischio)')

    # Creiamo la sorgente dati di Bokeh
    source = ColumnDataSource(df_bokeh)

    # Definiamo gli strumenti per l'interattività (Hover per vedere i dati)
    hover = HoverTool(
        tooltips=[
            ("ID", "@UserID"),
            ("Recency", "@Recency giorni"),
            ("Engagement Rate", "@Engagement_Rate{(0.00)}"),
            ("Punti Totali", "@Punti_Totali{0,0}"),
            ("Stato Simulato", "@Categoria")
        ]
    )

    # --- 3.2 Configurazione del Grafico ---

    # 1. Mappa dei colori (per distinguere Churned da Attivi)
    color_map = CategoricalColorMapper(factors=['CHURNED (Alto Rischio)', 'ATTIVO (Basso Rischio)'],
                                       palette=[Category10[3][0], Category10[3][2]])  # Rosso e Verde

    # 2. Creazione della Figura
    p = figure(
        height=350,
        width=650,
        title="Recency vs. Engagement Rate",
        x_axis_label="Recency (Giorni dall'Ultimo Accesso)",
        y_axis_label="Engagement Rate (Successo Task)",
        # Aggiungi gli strumenti di interazione
        tools=['pan, box_zoom, reset, save', hover]
    )

    # 3. Aggiunta dei punti (Glifi)
    p.scatter(
        x='Recency',
        y='Engagement_Rate',
        source=source,
        legend_field='Churn_Status',  # Usa la colonna per la legenda
        color={'field': 'Churn_Status', 'transform': color_map},
        alpha=0.6,
        size=8
    )

    # Spostamento della legenda in alto a sinistra
    p.legend.location = "top_right"
    p.legend.title = "Stato Churn Predetto"
    p.legend.label_text_font_size = "9pt"

    # --- 3.3 Visualizzazione in Streamlit ---
    st.bokeh_chart(p, use_container_width=True)

    st.caption("Ogni punto rappresenta un utente. Gli utenti a rischio *Churn* (rosso) si concentrano nell'angolo in basso a destra (alta Recency, basso Engagement).")

# --- Colonna 2: Simulazione e Predizione (La tua offerta di Servizio) ---
with col2:
    st.header("🔬 Simulazione Rischio Churn")
    st.markdown(
        "Simula un nuovo utente e vedi la probabilità di abbandono in base al suo comportamento.")

    # Input dell'utente tramite slider
    st.subheader("Input Comportamentali")

    # Usiamo valori medi o realistici come default
    recency = st.slider("Recency (Giorni dall'ultimo accesso)",
                        min_value=1, max_value=90, value=30, step=1)
    frequency = st.slider("Frequency (Accessi totali in 90gg)",
                          min_value=1, max_value=150, value=50, step=5)
    punti_totali = st.slider("Punti Totali Accumulati",
                             min_value=0, max_value=30000, value=5000, step=500)
    engagement_rate = st.slider("Engagement Rate (Task Completati / Totale Task)",
                                min_value=0.0, max_value=1.0, value=0.5, step=0.05)
    volatilita_punti = st.slider(
        "Volatilità Punti (Std Dev)", min_value=0, max_value=1000, value=200, step=50)
    task_completati = st.slider(
        "Task Completati", min_value=0, max_value=100, value=25, step=5)

    # Preparazione dei dati per la previsione
    input_data = {
        'Recency': recency,
        'Frequency': frequency,
        'Punti_Totali': punti_totali,
        'Engagement_Rate': engagement_rate,
        'Volatilita_Punti_Std': volatilita_punti,
        'Task_Completati': task_completati
    }

    # Bottone di Predizione
    if st.button("Calcola Rischio Churn"):
        prob = predict_churn(input_data)
        prob_percent = round(prob * 100, 2)

        st.markdown("---")
        st.subheader("Risultato della Predizione:")

        # Logica per l'interpretazione del rischio
        if prob >= 0.70:
            rischio_text = "MOLTO ALTO 🔴"
            st.error(
                f"Probabilità di Churn: **{prob_percent}%** ({rischio_text})")
        elif prob >= 0.40:
            rischio_text = "MODERATO 🟠"
            st.warning(
                f"Probabilità di Churn: **{prob_percent}%** ({rischio_text})")
        else:
            rischio_text = "BASSO 🟢"
            st.success(
                f"Probabilità di Churn: **{prob_percent}%** ({rischio_text})")

        st.markdown(
            f"**Insight:** L'utente presenta un rischio di abbandono del {prob_percent}%. Il modello suggerisce che un **alto valore di *Recency* ({recency} giorni)** è probabilmente la causa principale di questo rischio.")
