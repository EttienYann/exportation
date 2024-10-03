import joblib

# Nom du fichier du modèle que vous souhaitez tester
model_filename = "gbr_model.joblib"

# Tenter de charger le modèle
try:
    model = joblib.load(model_filename)
    print("Modèle chargé avec succès !")
    print(f"Informations sur le modèle : {model}")
except FileNotFoundError:
    print(f"Le fichier du modèle {model_filename} est introuvable.")
except Exception as e:
    print(f"Erreur lors du chargement du modèle : {e}")
