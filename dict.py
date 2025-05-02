import time
import requests
import json
import os
# Fetch contest data from AtCoder API
problem_models = requests.get('https://kenkoooo.com/atcoder/resources/problem-models.json').json()
# print('problem_models', problem_models)
merged_problems = requests.get('https://kenkoooo.com/atcoder/resources/merged-problems.json').json()
# print('merged_problems', merged_problems)
stats={}
chart={
    "abc":{},
    "arc":{},
    "agc":{},
    "others":{}
}
for stat in merged_problems:
    x="contest_id"
    if stat[x] not in stats :stats[stat[x]] = {}
    stats[stat[x]][stat["id"]]={}
    stats[stat[x]][stat["id"]]["name"]        =stat["name"]
    stats[stat[x]][stat["id"]]["point"]       =stat["point"]
    stats[stat[x]][stat["id"]]["solver_count"]=stat["solver_count"]
    if stat["id"] in problem_models:
        if "is_experimental" in problem_models[stat["id"]]:
            stats[stat[x]][stat["id"]]["is_experimental"]= problem_models[stat["id"]]["is_experimental"]
        if "variance" in problem_models[stat["id"]]:
            stats[stat[x]][stat["id"]]["variance"]   = problem_models[stat["id"]]["variance"]
        if "difficulty" in problem_models[stat["id"]]:
            stats[stat[x]][stat["id"]]["difficulty"] = problem_models[stat["id"]]["difficulty"]
            y=problem_models[stat["id"]]["difficulty"]
            if y<400: color="gray"
            elif y<800: color="brown"
            elif y<1200: color="green"
            elif y<1600: color="cyan"
            elif y<2000: color="blue"
            elif y<2400: color="yellow"
            elif y<2800: color="orange"
            elif y<3200: color="red"
            else: color="red"
            stats[stat[x]][stat["id"]]["color"] = color

for stat in stats:
    if "abc" in stat:x="abc"
    elif "arc" in stat:x="arc"
    elif "agc" in stat:x="agc"
    else: continue
    for i in stats[stat].values():
        # print(i)
        if ("color" not in i) or ("point" not in i): continue
        if i["point"]==None: continue
        if i["point"] not in chart[x]:chart[x][i["point"]]={}
        if i["color"] in chart[x][i["point"]]:
            chart[x][i["point"]][i["color"]]+=1
        else:
            chart[x][i["point"]][i["color"]]=1

os.makedirs('web-page/json', exist_ok=True)
# Save the stats dictionary to a JSON file
with open('web-page/json/stats.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)
# print(stats)
with open('web-page/json/chart.json', 'w', encoding='utf-8') as f:
    json.dump(chart, f, ensure_ascii=False, indent=2)
# print(chart)