from flask import Flask, request, jsonify
import re
import tensorflow as tf
import pickle
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()

# Charger le modèle et le tokenizer
model_path = "lstm_word2vec_model.h5"
tokenizer_path = "tokenizer.pkl"
model = tf.keras.models.load_model(model_path)
with open(tokenizer_path, 'rb') as f:
    tokenizer = pickle.load(f)

# Créer l'application Flask
app = Flask(__name__)
CORS(app)

# L'environnement des variables
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route('/')
def home():
    return "Bienvenu sur l'API d'analyse de sentiment"

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint pour faire des prédictions.
    Returns:
        json: Prédiction du modèle.
    """
    # Vérifier si la requête contient un JSON valide
    if not request.is_json:
        return jsonify({'error': 'Requête invalide. Le contenu doit être au format JSON.'}), 415

    data = request.json

    # Vérifier si le champ 'tweet' est présent et non vide
    if not data or 'tweet' not in data or not data['tweet'].strip():
        return jsonify({'error': 'Tweet vide ou manquant'}), 400

    tweet = data['tweet']

    # Prétraitement du tweet
    tweet_cleaned = re.sub(r'@\w+', '', tweet)  # Supprimer les mentions
    tweet_cleaned = re.sub(r'http\S+', '', tweet_cleaned)  # Supprimer les URLs
    tweet_cleaned = re.sub(r'[^a-zA-Z\s]', '', tweet_cleaned)  # Supprimer la ponctuation
    tweet_cleaned = tweet_cleaned.strip()

    # Tokenization et padding
    sequence = tokenizer.texts_to_sequences([tweet_cleaned])
    sequence = tf.keras.preprocessing.sequence.pad_sequences(sequence, maxlen=100)

    # Prédiction
    prediction = model.predict(sequence)
    sentiment = "Positif" if prediction[0][0] > 0.5 else "Négatif"

    return jsonify({'sentiment': sentiment})

# Démarrer l'API Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
