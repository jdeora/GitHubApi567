import requests
import json

def get_repo_commits(user_id):
    repos_url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(repos_url)
    repos = json.loads(response.text)

    for repo in repos:
        print(type(repo))
        repo_name = repo["name"]
        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        response = requests.get(commits_url)
        commits = json.loads(response.text)
        num_commits = len(commits)
        print(f"Repo: {repo_name} Number of commits: {num_commits}")

get_repo_commits("jdeora")








