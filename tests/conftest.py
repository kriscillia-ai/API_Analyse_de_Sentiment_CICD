import pytest
from unittest.mock import Mock

@pytest.fixture(autouse=True)
def mock_keras_load_model(monkeypatch):
    mock_model = Mock()
    monkeypatch.setattr('tensorflow.keras.models.load_model', lambda *args, **kwargs: mock_model)

@pytest.fixture
def app():
    from app import app
    return app
