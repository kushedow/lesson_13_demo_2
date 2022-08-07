import json
from json import JSONDecodeError

from project.exceptions import DataStorageError


class CandidatesDAO:

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataStorageError("path is broken")

    def _save_data(self, data):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file)

    #############################

    def get_all(self):
        return self._load_data()

    def get_by_pk(self, pk) -> dict | None:
        for candidate in self._load_data():
            if candidate["pk"] == pk:
                return candidate

    def delete_by_pk(self, pk):
        candidates = self._load_data()
        for can in candidates:
            if can["pk"] == pk:
                candidates.remove(can)
                self._save_data(candidates)
                return True
        return False



    def get_by_skill(self, skill):
        pass


    def get_by_name(self, name):
        pass


