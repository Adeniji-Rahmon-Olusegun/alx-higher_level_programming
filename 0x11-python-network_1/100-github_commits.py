#!/usr/bin/python3

"""
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    commits = {'per_page': 10}

    res = requests.get(url, params=commits)

    if res.status_code == 200:
        commit_messages = res.json()
        for commit in commit_messages:
            sha = commit['sha']
            name = commit['commit']['author']['name']
            print(f"{sha}: {name}")
