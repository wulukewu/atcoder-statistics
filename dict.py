import time
import requests
import json
import os

print("\n=== AtCoder Statistics Data Collection ===")
print("Fetching data from AtCoder API...")

# Fetch contest data from AtCoder API
problem_models = requests.get('https://kenkoooo.com/atcoder/resources/problem-models.json').json()
print(f"✓ Loaded {len(problem_models)} problem models")
merged_problems = requests.get('https://kenkoooo.com/atcoder/resources/merged-problems.json').json()
print(f"✓ Loaded {len(merged_problems)} merged problems")

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

print("\nProcessing problems and organizing by contest type...")
contest_counts = {"abc": 0, "arc": 0, "agc": 0, "others": 0}
problem_counts = {"abc": 0, "arc": 0, "agc": 0, "others": 0}

# Process each problem and organize by contest type
# Build stats, chart, and problem_dict in a single pass for efficiency
for idx, problem in enumerate(merged_problems):
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
        contest_counts[contest_type] += 1
    
    # Build problem entry with basic info
    problem_entry = {
        "name": problem["name"],
        "point": problem["point"],
        "solver_count": problem["solver_count"]
    }
    
    # Add problem model data if available
    model = problem_models.get(problem_id)
    if model:
        if "is_experimental" in model:
            problem_entry["is_experimental"] = model["is_experimental"]
        if "variance" in model:
            problem_entry["variance"] = model["variance"]
        if "difficulty" in model:
            problem_entry["difficulty"] = model["difficulty"]
            color = get_color(model["difficulty"])
            if color:
                problem_entry["color"] = color
    
    stats[contest_type][contest_id][problem_id] = problem_entry
    problem_counts[contest_type] += 1
    
    # Build chart and problem_dict in the same pass if problem has color and point
    if "color" in problem_entry and "point" in problem_entry and problem_entry["point"] is not None:
        point = problem_entry["point"]
        color = problem_entry["color"]
        
        # Update chart data
        if point not in chart[contest_type]:
            chart[contest_type][point] = {}
        chart[contest_type][point][color] = chart[contest_type][point].get(color, 0) + 1
        
        # Update problem dictionary
        problem_dict[contest_type].setdefault(point, {}).setdefault(color, []).append(problem_id)

print("\nContest Statistics:")
for contest_type in ["abc", "arc", "agc", "others"]:
    print(f"  {contest_type.upper()}: {contest_counts[contest_type]} contests, {problem_counts[contest_type]} problems")

# Ensure output directory exists
os.makedirs('web-page/json', exist_ok=True)

print("\nSaving data to JSON files...")
# Save the stats and chart dictionaries to JSON files
with open('web-page/json/stats.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)
print("✓ Saved stats.json")

with open('web-page/json/chart.json', 'w', encoding='utf-8') as f:
    json.dump(chart, f, ensure_ascii=False, indent=2)
print("✓ Saved chart.json")

with open('web-page/json/problem_dict.json', 'w', encoding='utf-8') as f:
    json.dump(problem_dict, f, ensure_ascii=False, indent=2)
print("✓ Saved problem_dict.json")

print("\n=== Data Collection Complete ===")