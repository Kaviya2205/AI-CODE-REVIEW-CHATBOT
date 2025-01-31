import requests
from config import GITHUB_TOKEN

def fetch_pr_files(repo: str, pr_number: int):
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/files"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to fetch PR files")
    return response.json()

def post_github_comment(repo: str, pr_number: int, comment: dict):
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/comments"
    requests.post(url, json=comment, headers=headers)
