from controllers.base import Base_Controller
from utils.api import get_data_from_url
import os


class Github_Controller(Base_Controller):   # operations of GitHub API
    def __init__(self, id="github", base_url="https://api.github.com",
                 token_name="GITHUB_ACCESS_TOKEN",
                 username_name="GITHUB_USERNAME",
                 **kwargs) -> None:
        super().__init__(id, base_url, token_name, username_name, **kwargs)
        self.headers = {
            'Authorization': 'Bearer {}'.format(self.token),
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }
        self.repos = []
        self.language_repo = {}
        self.language_count = {}
        self.language_percentage = {}

    def init(self):
        print("INIT GITHUB")
        self.get_all_repo()
        self.get_language_repo()
        self.get_language_count()
        self.get_language_percentage()

    # get name list of all repos
    def get_all_repo(self) -> list:
        url = os.path.join(self.base_url, "users/{}/repos".format(self.username))
        status, data = get_data_from_url(url, self.headers)
        self.repos = data if status == 200 else self.repos
        return self.repos

    # get the bytes count of each language used in a repo
    def get_language_repo(self) -> dict:
        repo_names = [repo["name"] for repo in self.repos]
        for repo_name in repo_names:
            url = os.path.join(self.base_url, "repos/{}/{}/languages".format(self.username, repo_name))
            status, data = get_data_from_url(url, self.headers)
            if status == 200:
                self.language_repo[repo_name] = data
        return self.language_repo
    
    # get bytes count of each language in all repos
    def get_language_count(self) -> dict:
        total_language_dict = {}
        for repo, language_dict in self.language_repo.items():
            for language, byte_number in language_dict.items():
                if language not in total_language_dict:
                    total_language_dict[language] = byte_number
                else:
                    total_language_dict[language] += byte_number
        self.language_count = total_language_dict
        return total_language_dict
    
    # get percentage of each language (by bytes count) in all repos
    def get_language_percentage(self) -> dict:
        total_bytes = sum(self.language_count.values())
        if not total_bytes:
            return {}
        for language, count in self.language_count.items():
            self.language_percentage[language] = round(count / total_bytes * 100, 2) 
        return self.language_percentage