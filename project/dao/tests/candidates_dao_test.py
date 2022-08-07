import pytest as pytest
from project.dao.candidates_dao import CandidatesDAO

class TestCandidatesDAO:

    @pytest.fixture
    def candidates_dao(self):
        mock_path = "tests/mock/candidates.mock.json"
        instance = CandidatesDAO(mock_path)
        return instance

    def test_get_all(self, candidates_dao):
        all = candidates_dao.get_all()
        assert type(all) == list
        assert len(all) == 2

    pks_and_full_names = [

        (1, "Sheri Torres"),
        (2, "Burt Stein"),
    ]

    @pytest.mark.parametrize("pk, correct_name", pks_and_full_names)
    def test_get_by_pk(self, candidates_dao, pk, correct_name):
        can = candidates_dao.get_by_pk(pk)
        assert can["full_name"] == correct_name, "Получен неверный кандидит по пк"




