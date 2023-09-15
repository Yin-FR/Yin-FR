from controllers.base import Base_Controller
from utils.api import get_data_from_url
import base64

import os
import base64


class Wakatime_Controller(Base_Controller):
    def __init__(self, id="wakatime", base_url="https://wakatime.com/api/v1", token_name="WAKA_SECRET", username_name="", **kwargs) -> None:
        super().__init__(id, base_url, token_name, username_name, **kwargs)
        self.headers = {
            'Authorization': 'Basic {}'.format(base64.b64encode(self.token.encode()).decode()),
        }
        self.total_time = {}
        self.language_week = {}

    def init(self):
        self.get_total_time()
        self.get_language_week()

    # The total time logged since account created, available even for Free accounts.
    def get_total_time(self) -> dict:
        url = os.path.join(self.base_url, "users/current/all_time_since_today")
        status, data = get_data_from_url(url, self.headers)
        self.total_time = data["data"] if status == 200 else self.total_time
        return self.total_time
    
    # The time spent on each language and its percentage
    def get_language_week(self) -> dict:
        url = os.path.join(self.base_url, "users/current/stats/last_7_days")
        status, data = get_data_from_url(url, self.headers)
        language_week = data["data"]["languages"] if status == 200 else []
        if not len(language_week):
            return {}
        total_time = sum(float(language["decimal"]) for language in language_week)
        for language in language_week:
            self.language_week[language["name"]] = {
                "time": language["text"],
                "percentage": round(float(language["decimal"]) / total_time * 100, 2)
            }
        return self.language_week