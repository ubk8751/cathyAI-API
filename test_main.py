import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
import httpx
from main import app

client = TestClient(app)


def test_health_backend_up():
    with patch("main.httpx.AsyncClient") as mock_client:
        mock_get = Mock()
        mock_client.return_value.__aenter__.return_value.get = mock_get
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["ok"] is True


def test_health_backend_down():
    with patch("main.httpx.AsyncClient") as mock_client:
        mock_client.return_value.__aenter__.return_value.get.side_effect = Exception("Connection failed")
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["backend_status"] == "down"


def test_models_backend_unavailable():
    with patch("main.httpx.AsyncClient") as mock_client:
        mock_client.return_value.__aenter__.return_value.get.side_effect = httpx.RequestError("Connection failed")
        response = client.get("/models")
        assert response.status_code == 503
        assert "Backend unavailable" in response.json()["detail"]
