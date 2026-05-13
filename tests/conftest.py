import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "back"))

import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture(scope="session")
def client():
    """
    Один TestClient на всю pytest-сессию.
    `with` запускает lifespan приложения (create_db и т.п.)
    и держит один event loop, чтобы engine не отвязался.
    """
    with TestClient(app) as c:
        yield c