import streamlit as st
import pandas as pd
import joblib
import sklearn

# CHARGEMENT DES MODELS
model_files = {
    "Modèle GBR pour CAFE": "gbr_model.joblib"
}

# Barre de navigation pour sélectionner un modèle
st.sidebar.title("Navigation")
model_choice = st.sidebar.selectbox("Choisissez un modèle :", list(model_files.keys()))

# Chargement du modèle sélectionné
model_filename = model_files[model_choice]
try:
    model = joblib.load(model_filename)
    st.sidebar.success(f"Modèle {model_choice} chargé avec succès.")
    
    # Vérifier et afficher la version de scikit-learn
    st.sidebar.write(f"Version de scikit-learn : {sklearn.__version__}")
except FileNotFoundError:
    st.sidebar.error(f"Le fichier du modèle {model_choice} est introuvable.")
    st.stop()
