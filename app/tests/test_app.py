import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import create_app

def setup_client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()

def test_home_returns_service_name():
    response = setup_client().get("/")
    assert response.status_code == 200
    assert response.get_json()["name"] == "CloudOps DevOps Platform"

def test_health_endpoint():
    response = setup_client().get("/healthz")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_info_endpoint():
    response = setup_client().get("/api/info")
    assert response.status_code == 200
    assert response.get_json()["service"] == "cloudops-api"

def test_unknown_route_returns_json_404():
    response = setup_client().get("/does-not-exist")
    assert response.status_code == 404
    assert response.get_json()["error"] == "not found"
