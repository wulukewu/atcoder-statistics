import time
import requests
import json
import os
# Fetch contest data from AtCoder API
# contest_problems = requests.get('https://kenkoooo.com/atcoder/resources/contest-problem.json').json()
# print('contest_problems', contest_problems)
problem_models = requests.get('https://kenkoooo.com/atcoder/resources/problem-models.json').json()
# print('problem_models', problem_models)
merged_problems = requests.get('https://kenkoooo.com/atcoder/resources/merged-problems.json').json()
# print('merged_problems', merged_problems)
stats={}
for stat in merged_problems:
    stats[stat["id"]] = {}
    stats[stat["id"]]["contest_id"]  =stat["contest_id"]
    stats[stat["id"]]["name"]        =stat["name"]
    stats[stat["id"]]["point"]       =stat["point"]
    stats[stat["id"]]["solver_count"]=stat["solver_count"]
    if stat["id"] in problem_models:
        if "is_experimental" in problem_models[stat["id"]]:
            stats[stat["id"]]["is_experimental"]= problem_models[stat["id"]]["is_experimental"]
        if "variance" in problem_models[stat["id"]]:
            stats[stat["id"]]["variance"]   = problem_models[stat["id"]]["variance"]
        if "difficulty" in problem_models[stat["id"]]:
            stats[stat["id"]]["difficulty"] = problem_models[stat["id"]]["difficulty"]
            if problem_models[stat["id"]]["difficulty"]<400: color="gray"
            elif problem_models[stat["id"]]["difficulty"]<800: color="brown"
            elif problem_models[stat["id"]]["difficulty"]<1200: color="green"
            elif problem_models[stat["id"]]["difficulty"]<1600: color="cyan"
            elif problem_models[stat["id"]]["difficulty"]<2000: color="blue"
            elif problem_models[stat["id"]]["difficulty"]<2400: color="yellow"
            elif problem_models[stat["id"]]["difficulty"]<2800: color="orange"
            elif problem_models[stat["id"]]["difficulty"]<3200: color="red"
            else: color="red"
            stats[stat["id"]]["color"] = color
os.makedirs('web-page/json', exist_ok=True)
# Save the stats dictionary to a JSON file
with open('web-page/json/stats.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)
# print(stats)