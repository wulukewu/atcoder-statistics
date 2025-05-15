import time
import requests
import json
import os

# Fetch contest data from AtCoder API
problem_models = requests.get('https://kenkoooo.com/atcoder/resources/problem-models.json').json()
print(f"Loaded {len(problem_models)} problem models")
merged_problems = requests.get('https://kenkoooo.com/atcoder/resources/merged-problems.json').json()
print(f"Loaded {len(merged_problems)} merged problems")

# Initialize data structures for statistics and chart data
stats = {
    "abc": {},
    "arc": {},
    "agc": {},
    "others": {}
}
chart = {
    "abc": {},
    "arc": {},
    "agc": {},
    "others": {}
}
problem_dict = {
    "abc": {},
    "arc": {},
    "agc": {},
    "others": {}
}

# Helper function to determine color from difficulty
COLOR_THRESHOLDS = [
    (400, "grey"),
    (800, "brown"),
    (1200, "green"),
    (1600, "cyan"),
    (2000, "blue"),
    (2400, "yellow"),
    (2800, "orange"),
    (3200, "red"),
    (3600, "bronze"),
    (4000, "silver"),
    (4400, "gold")
]
def get_color(difficulty):
    if difficulty is None:
        return None
    for threshold, color in COLOR_THRESHOLDS:
        if difficulty < threshold:
            return color
    return "red"

# Process each problem and organize by contest type
for idx, problem in enumerate(merged_problems):
    # Print first 5 problems for debugging
    if idx < 5:
        print(f"Processing problem: {problem['id']} in contest {problem['contest_id']}")
    # Determine contest type
    if "abc" in problem["contest_id"]:
        contest_type = "abc"
    elif "arc" in problem["contest_id"]:
        contest_type = "arc"
    elif "agc" in problem["contest_id"]:
        contest_type = "agc"
    else:
        contest_type = "others"
    contest_id = problem["contest_id"]
    problem_id = problem["id"]

    # Initialize contest entry if needed
    if contest_id not in stats[contest_type]:
        stats[contest_type][contest_id] = {}
    stats[contest_type][contest_id][problem_id] = {
        "name": problem["name"],
        "point": problem["point"],
        "solver_count": problem["solver_count"]
    }

    # Add problem model data if available
    if problem_id in problem_models:
        model = problem_models[problem_id]
        if "is_experimental" in model:
            stats[contest_type][contest_id][problem_id]["is_experimental"] = model["is_experimental"]
        if "variance" in model:
            stats[contest_type][contest_id][problem_id]["variance"] = model["variance"]
        if "difficulty" in model:
            stats[contest_type][contest_id][problem_id]["difficulty"] = model["difficulty"]
            color = get_color(model["difficulty"])
            if color:
                stats[contest_type][contest_id][problem_id]["color"] = color
                # Print color assignment for first 5 problems
                if idx < 5:
                    print(f"Problem {problem_id} difficulty: {model['difficulty']}, assigned color: {color}")

# Build chart data: count problems by point and color
for contest_type in stats:
    for contest_id in stats[contest_type]:
        for problem in stats[contest_type][contest_id].values():
            if "color" not in problem or "point" not in problem or problem["point"] is None:
                continue
            point = problem["point"]
            color = problem["color"]
            if point not in chart[contest_type]:
                chart[contest_type][point] = {}
            if color in chart[contest_type][point]:
                chart[contest_type][point][color] += 1
            else:
                chart[contest_type][point][color] = 1

for contest_type in stats:
    for contest_id in stats[contest_type]:
        for problem_id in stats[contest_type][contest_id]:
            if "color" not in stats[contest_type][contest_id][problem_id] or "point" not in stats[contest_type][contest_id][problem_id] or stats[contest_type][contest_id][problem_id]["point"] is None:
                continue
            point = stats[contest_type][contest_id][problem_id]["point"]
            color = stats[contest_type][contest_id][problem_id]["color"]
            problem_dict[contest_type].setdefault(point, {}).setdefault(color, []).append(problem_id)

# Ensure output directory exists
os.makedirs('web-page/json', exist_ok=True)

print("Saving stats and chart data to JSON files...")
# Save the stats and chart dictionaries to JSON files
with open('web-page/json/stats.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)
with open('web-page/json/chart.json', 'w', encoding='utf-8') as f:
    json.dump(chart, f, ensure_ascii=False, indent=2)
with open('web-page/json/problem_dict.json', 'w', encoding='utf-8') as f:
    json.dump(problem_dict, f, ensure_ascii=False, indent=2)