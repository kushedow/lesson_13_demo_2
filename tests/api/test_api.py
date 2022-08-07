import pytest
from project.app import app

@pytest.fixture
def test_client():
    app.config["DATA_SOURCE"] = "tests/mock/candidates.mock.json"
    return app.test_client()

def test_candidate_all_view(test_client):

    all_candidates = test_client.get("/").get_json()
    print(all_candidates)
    assert type(all_candidates) == list

# def test_candidate_single_view(test_client):
#     pass
