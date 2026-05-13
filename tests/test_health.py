def test_health_return_200(client):
    # Act — делаем GET-запрос на /health
    response = client.get("/health")
    # Assert — проверяем что вернулось то, что мы ожидаем
    assert response.status_code == 200

def test_health_returns_ok_status(client):
    response = client.get("/health")
    data = response.json()
    assert data["status"] == "ok"

def test_health_reports_db_ok(client):
    response = client.get("/health")
    data = response.json()
    assert data["db"] == "ok"