# API_Analyse_de_Sentiment_CICD

## **Projet : Anticiper les Bad Buzz - Analyse de Sentiment de Tweets**

Ce projet vise à développer une solution d'intelligence artificielle (IA) complète pour l'analyse de sentiment de tweets, permettant aux entreprises (comme Air Paradis dans ce cas d'étude) d'anticiper et de gérer proactivement les bad buzz sur les réseaux sociaux.

-----

### **Fonctionnalités Clés :**

  * **Analyse de Sentiment Avancée :** Détection du sentiment (positif, négatif, neutre) des tweets en utilisant des modèles de **Deep Learning (LSTM)** avec **Word Embeddings** (Word2Vec, GloVe, FastText) et exploration de **BERT**.
  * **Pipeline MLOps Robuste :** Intégration de **MLflow** pour le suivi des expérimentations, la gestion des modèles et la visualisation des métriques.
  * **Déploiement Continu (CI/CD) :** Automatisation complète du build, des tests unitaires et du déploiement de l'API via **GitHub Actions** vers **Google Cloud Run**.
  * **Surveillance en Production :** Utilisation d'**Azure Application Insights** pour le monitoring en temps réel, la remontée de traces des prédictions incorrectes et le déclenchement d'alertes par e-mail en cas de performances dégradées.
  * **Interface Utilisateur de Test :** Une application **Streamlit** conviviale pour interagir avec l'API, soumettre des tweets et recueillir des retours utilisateur sur la pertinence des prédictions.

-----

### **Architecture du Projet :**

Le projet suit une architecture MLOps, garantissant la reproductibilité, la scalabilité et la maintenance du modèle en production :

1.  **Exploration & Modélisation (Notebooks) :** Développement et entraînement de différents modèles NLP (Régression Logistique, LSTM, BERT).
2.  **Tracking des Expériences :** MLflow pour centraliser les métriques et artefacts de chaque expérimentation.
3.  **API de Prédiction :** Une API Flask exposant le modèle entraîné, déployée en tant que service conteneurisé.
4.  **Déploiement Automatisé :** GitHub Actions pour le CI/CD vers Google Cloud Run.
5.  **Monitoring & Alerting :** Azure Application Insights pour le suivi des performances et la détection des anomalies.
6.  **Interface de Feedback :** Streamlit pour l'interaction utilisateur et la collecte de données pour l'amélioration continue.

-----

### **Technologies Utilisées :**

  * **Langages :** Python
  * **Machine Learning / Deep Learning :** TensorFlow, Keras, scikit-learn, Hugging Face Transformers
  * **NLP :** NLTK, SpaCy
  * **MLOps :** MLflow
  * **Web Framework :** Flask
  * **Conteneurisation :** Docker
  * **CI/CD :** GitHub Actions
  * **Cloud Computing :** Google Cloud Run
  * **Monitoring :** Azure Application Insights
  * **Interface Utilisateur :** Streamlit
  * **Version Control :** Git, GitHub

-----

### **Mise en Route :**

Pour exécuter ce projet en local ou le déployer, veuillez consulter les instructions détaillées dans le dossier `docs/` (ou directement dans les notebooks si vous n'avez pas un dossier `docs` dédié).

-----

### **Structure du Dépôt :**

  * `notebooks/` : Notebooks Jupyter pour l'EDA, la modélisation et l'expérimentation.
  * `app/` : Code source de l'API Flask et Dockerfile.
  * `streamlit_app/` : Code source de l'application Streamlit.
  * `tests/` : Tests unitaires.
  * `requirements.txt` : Liste des dépendances Python.
  * `README.md` : Ce fichier.
