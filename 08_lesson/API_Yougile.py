import requests


class API:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def create_project(self, title, user_id):
        company = {
            "title": title,
            "users": {user_id: "admin"}
        }
        resp = requests.post(
            f"{self.base_url}/api-v2/projects",
            json=company,
            headers=self.headers
        )
        return resp

    def update_project(self, project_id, data):
        resp = requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            json=data,
            headers=self.headers
        )
        return resp

    def get_project(self, project_id):
        resp = requests.get(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers
        )
        return resp

    def delete_project(self, project_id):
        resp = requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            json={"deleted": True},
            headers=self.headers
        )
        return resp
