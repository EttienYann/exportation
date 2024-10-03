import streamlit as st
import pandas as pd
import joblib

# CHARGEMENT DES MODELS
model_files = {
    "Modèle RF pour le Cacao": "rf8model.joblib",
    "Modèle SVR pour le Cacao": "svr_model_c.joblib"
}
st.title('fait par AYEBIE MESHAC ')
# Barre de navigation pour sélectionner un modèle
st.sidebar.title("Navigation")
model_choice = st.sidebar.selectbox("Choisissez un modèle :", list(model_files.keys()))

# Chargement du modèle sélectionné
model_filename = model_files[model_choice]
try:
    model = joblib.load(model_filename)
    
    st.sidebar.success(f"Modèle {model_choice} chargé avec succès.")
except FileNotFoundError:
    st.sidebar.error(f"Le fichier du modèle {model_choice} est introuvable.")
    st.stop()

# Interface utilisateur principale
st.title(f'Prédiction avec {model_choice}')

# Exemple d'entrée de données
input_data = {
    'pib_milliard_fcfa': st.number_input("PIB (Milliards FCFA)", min_value=0.0, step=0.1),
    'prix_pro_cacao/kg': st.number_input("Prix Pro Cacao (par kg)", min_value=0.0, step=0.1),
    'prix_pro_cafe/kg': st.number_input("Prix Pro Café (par kg)", min_value=0.0, step=0.1),
    'valeur_var_temp': st.number_input("Valeur Variation Temp.", min_value=-50.0, step=0.1),
    'taux_change': st.number_input("Taux de Change", min_value=0.0, step=0.1),
    'pro_cafe_tonne': st.number_input("Production Café (tonnes)", min_value=0, step=1),
    'pro_cacao_tonne': st.number_input("Production Cacao (tonnes)", min_value=0, step=1),
    'export_binome': st.number_input("Export Binôme", min_value=0, step=1),
    'Croissance_valeur_export_europe': st.number_input("Croissance Valeur Export Europe", min_value=0.0, step=0.1),
    'Croissance_valeur_export_afrique': st.number_input("Croissance Valeur Export Afrique", min_value=0.0, step=0.1),
    'Croissance_valeur_export_uemoa': st.number_input("Croissance Valeur Export UEMOA", min_value=0.0, step=0.1),
    'Croissance_valeur_export_cedeao': st.number_input("Croissance Valeur Export CEDEAO", min_value=0.0, step=0.1),
    'Croissance_valeur_export_amerique': st.number_input("Croissance Valeur Export Amérique", min_value=0.0, step=0.1),
    'Croissance_valeur_export_asie': st.number_input("Croissance Valeur Export Asie", min_value=0.0, step=0.1)
}

# Convertir les données d'entrée en DataFrame
input_df = pd.DataFrame([input_data])

# Afficher les données d'entrée
st.write("Données d'entrée :", input_df)

# Si l'utilisateur clique sur le bouton de prédiction
if st.button('Prédire'):
    # Faire une prédiction avec le modèle chargé
    try:
        prediction = model.predict(input_df)
        st.success(f'La prédiction est : {prediction[0]}')
    except Exception as e:
        st.error(f"Erreur lors de la prédiction : {e}")
