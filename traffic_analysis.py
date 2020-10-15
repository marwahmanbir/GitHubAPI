from github import Github
import os
from pprint import pprint
from operator import itemgetter

token = os.getenv('GITHUB_TOKEN')
g = Github(token)
repo = g.get_repo("marwahmanbir/OpenEDU")
clones = repo.get_clones_traffic(per="week")
views = repo.get_views_traffic(per="week")

print(f"Repository has {clones['count']} clones out of which {clones['uniques']} are unique.")
print(f"Repository has {views['count']} views out of which {views['uniques']} are unique.")

best_week = max(*list((week.count, week.timestamp) for week in views["views"]), key=itemgetter(0))

pprint(views)
print(f"Repository had most views in {best_week[1]} with {best_week[0]} views")