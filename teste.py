from fastapi.testclient import TestClient
from main import app

cliente = TestClient(app)

def test_health_check():
    response = cliente.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_metricas():
    response = cliente.get("/metricas")
    assert response.status_code == 200
    dados = response.json()
    assert "quantidade_tarefas" in dados
    assert "tarefas_finalizadas" in dados
    assert "tarefas_pendentes" in dados