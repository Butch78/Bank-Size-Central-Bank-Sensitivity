from fastapi.testclient import TestClient
import pytest
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from app.main import app
from app.utils.deps import get_session

client = TestClient(app)

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_create_deposit_rate():
    response = client.post(
        "/target_ranges/",
        json={
  "date": "2023-12-15T09:52:24.810Z",
  "lower_bound": 0.1,
  "upper_bound": 0.1
},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["date"] == "2023-12-15T09:52:24.810000"
    assert data["lower_bound"] == 0.1
    assert data["upper_bound"] == 0.1
    assert "id" in data

