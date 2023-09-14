import os


class Base_Controller:
    def __init__(self, id, base_url, token_name, username_name, **kwargs) -> None:
        self.id = id
        self.base_url = base_url
        self.token_name = token_name
        self.username_name = username_name

        for k, w in kwargs.items():
            self[k] = w

        self.username = os.getenv(self.username_name)
        self.token = os.getenv(self.token_name)

        self.headers = {}
    
