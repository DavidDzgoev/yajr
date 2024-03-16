import json

import requests


class JudoBaseApi:
    """Represents API functionality."""

    def __init__(self):
        self.base_url = "https://data.ijf.org/api/"

    def get_json(self, params):
        """Makes get request to specified api and returns json"""
        response = requests.get(
            self.base_url + "get_json",
            params=params,
            verify=False,
        )
        if response.status_code != 200:
            raise ConnectionError(f"{response.status_code}")

        return json.loads(response.text)

    def get_competition_list(self, year: str = "", month: str = ""):
        """Returns competition list by specified filters"""

        params = {
            "params[action]": "competition.get_list",
            "params[year]": year,
            "params[month]": month,
            "params[sort]": -1,
            "params[limit]": 5000,
        }
        return self.get_json(params)

    def find_contest(self, id_competition: str = "", id_weight: str = "", id_person: str = ""):
        """Returns contest list by specified filters"""

        params = {
            "params[action]": "contest.find",
            "params[id_competition]": id_competition,
            "params[id_weight]": id_weight,
            "params[id_person]": id_person,
            "params[order_by]": "cnum",
            "params[limit]": 5000,
        }
        return self.get_json(params)["contests"]

    def competitor_info(self, id_person: str = ""):
        """Returns contest list by specified filters"""

        params = {
            "params[action]": "competitor.info",
            "params[id_person]": id_person,
        }
        return self.get_json(params)

    def competiton_info(self, id_competition: str = ""):
        """Returns contest list by specified filters"""

        params = {
            "params[action]": "competition.info",
            "params[id_competition]": id_competition,
        }
        return self.get_json(params)

print(JudoBaseApi().find_contest(id_person="9396"))
