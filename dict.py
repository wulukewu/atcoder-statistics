import time
import requests
import json
import os
# Fetch contest data from AtCoder API
problem_models = requests.get('https://kenkoooo.com/atcoder/resources/problem-models.json').json()
# print('problem_models', problem_models)
merged_problems = requests.get('https://kenkoooo.com/atcoder/resources/merged-problems.json').json()
# print('merged_problems', merged_problems)
stats={
    "abc":{},
    "arc":{},
    "agc":{},
    "others":{}
}
chart={
    "abc":{},
    "arc":{},
    "agc":{},
    "others":{}
}
for stat in merged_problems:
    y="others"
    if "abc" in stat["contest_id"]: y="abc"
    elif "arc" in stat["contest_id"]: y="arc"
    elif "agc" in stat["contest_id"]: y="agc"
    else: y="others"
    x="contest_id"
    if stat[x] not in stats[y] :stats[y][stat[x]] = {}
    stats[y][stat[x]][stat["id"]]={}
    stats[y][stat[x]][stat["id"]]["name"]        =stat["name"]
    stats[y][stat[x]][stat["id"]]["point"]       =stat["point"]
    stats[y][stat[x]][stat["id"]]["solver_count"]=stat["solver_count"]
    if stat["id"] in problem_models:
        if "is_experimental" in problem_models[stat["id"]]:
            stats[y][stat[x]][stat["id"]]["is_experimental"]= problem_models[stat["id"]]["is_experimental"]
        if "variance" in problem_models[stat["id"]]:
            stats[y][stat[x]][stat["id"]]["variance"]   = problem_models[stat["id"]]["variance"]
        if "difficulty" in problem_models[stat["id"]]:
            stats[y][stat[x]][stat["id"]]["difficulty"] = problem_models[stat["id"]]["difficulty"]
            z=problem_models[stat["id"]]["difficulty"]
            if z == None: continue
            if z<400: color="grey"
            elif z<800: color="brown"
            elif z<1200: color="green"
            elif z<1600: color="cyan"
            elif z<2000: color="blue"
            elif z<2400: color="yellow"
            elif z<2800: color="orange"
            elif z<3200: color="red"
            else: color="red"
            stats[y][stat[x]][stat["id"]]["color"] = color
    # if stat["point"]==100: print(stats[y][stat[x]][stat["id"]])

for x in stats:
    for stat in stats[x]:
        # print(stat)
        for i in stats[x][stat].values():
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