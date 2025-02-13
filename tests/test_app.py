import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# Ajoute le répertoire racine du projet au PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# tests/test_app.py
import pytest
from app import app  # Importe l'application Flask


@pytest.fixture
def client():
    """
    Crée un client de test pour l'application Flask.
    """
    app.config['TESTING'] = True  # Active le mode test
    with app.test_client() as client:
        yield client


def test_predict_positive(client):
    """
    Teste la route /predict avec un tweet positif.
    """
    response = client.post('/predict', json={'tweet': 'I love this product!'})
    assert response.status_code == 200  # Vérifie que la réponse est OK
    assert response.json == {'sentiment': 'Positif'}  # Vérifie la prédiction


def test_predict_negative(client):
    """
    Teste la route /predict avec un tweet négatif.
    """
    response = client.post('/predict', json={'tweet': 'I hate this product!'})
    assert response.status_code == 200
    assert response.json == {'sentiment': 'Négatif'}


def test_predict_empty_tweet(client):
    """
    Teste la route /predict avec un tweet vide.
    """
    response = client.post('/predict', json={'tweet': ''})

    # Modification : vérifie que l'application renvoie une erreur 400 pour un tweet vide
    assert response.status_code == 400  # Vérifie que la réponse est une erreur
    assert 'error' in response.json  # Vérifie que le message d'erreur est présent
    assert response.json['error'] == 'Tweet vide ou manquant'


def test_predict_invalid_input(client):
    """
    Teste la route /predict avec une entrée invalide (pas un JSON).
    """
    response = client.post('/predict', data="Not a JSON")

    # Modification : attend maintenant un code de statut 415 (Unsupported Media Type)
    assert response.status_code == 415  # Vérifie que le type de contenu est incorrect
