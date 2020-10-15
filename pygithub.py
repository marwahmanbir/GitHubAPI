from github import Github
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN')
g = Github(token)
repo = g.get_repo("marwahmanbir/OpenEDU")
issues = repo.get_issues(state="open")
pulls = repo.get_pulls(state="open")
pprint(issues.get_page(0))
pprint(pulls.get_page(0))