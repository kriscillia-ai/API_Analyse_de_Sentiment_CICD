import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_model():
    return Mock()

@pytest.fixture
def mock_tf(monkeypatch):
    mock_tf = Mock()
    mock_tf.keras.models.load_model.return_value = mock_model()
    monkeypatch.setattr('app.tf', mock_tf)
    return mock_tf
