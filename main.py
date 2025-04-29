import requests
import json
import math
import time

def update_statics(diff, color, statics):
    if diff in statics:
        if color in statics[diff]:
            statics[diff][color] += 1
        else:
            statics[diff][color] = 1
    else:
        statics[diff] = {}
        statics[diff][color] = 1


def clip_difficulty(difficulty):
    if difficulty < 0:
        return 0
    elif difficulty > 1000:
        return 1000
    else:
        return difficulty


def get_rating_color(rating):
    if rating < 400:
        return "grey"
    elif rating < 800:
        return "brown"
    elif rating < 1200:
        return "green"
    elif rating < 1600:
        return "cyan"
    elif rating < 2000:
        return "blue"
    elif rating < 2400:
        return "yellow"
    elif rating < 2800:
        return "orange"
    else:
        return "red"


# Define colors and color codes
statics = {}
colors = ["grey", "brown", "green", "cyan", "blue", "yellow", "orange", "red"]
color_codes = {
    "grey": "#6b7280",  # --gray-500
    "brown": "#a16207",  # --brown
    "green": "#22c55e",  # --green
    "cyan": "#06b6d4",  # --cyan
    "blue": "#3b82f6",  # --blue
    "yellow": "#eab308",  # --yellow
    "orange": "#f97316",  # --orange
    "red": "#ef4444",  # --red
}

latest_problem = "ABC000"  # Default value in case of error

try:
    # Fetch problem models with difficulty ratings
    print("Fetching problem models with difficulty ratings...")
    models_response = requests.get("https://kenkoooo.com/atcoder/resources/problem-models.json")
    problem_models = models_response.json()
    print(f"Found {len(problem_models)} problem models")

    # Also fetch problems data for additional information
    print("Fetching problems data...")
    problems_response = requests.get("https://kenkoooo.com/atcoder/resources/problems.json")
    problems = {p["id"]: p for p in problems_response.json()}
    print(f"Found {len(problems)} problems")

    # Fetch merged problems data which contains point values
    print("Fetching merged problems data...")
    merged_problems_response = requests.get("https://kenkoooo.com/atcoder/resources/merged-problems.json")
    merged_problems = {p["id"]: p for p in merged_problems_response.json()}
    print(f"Found {len(merged_problems)} merged problems")

    # Also fetch contest information to identify ABC contests
    print("Fetching contest information...")
    contests_response = requests.get("https://kenkoooo.com/atcoder/resources/contests.json")
    contests = {c["id"]: c for c in contests_response.json()}

    # Find the latest ABC contest
    abc_contests = [contest for contest in contests.values() if contest["title"].startswith("AtCoder Beginner Contest")]
    latest_abc = max(abc_contests, key=lambda x: int(x["title"].replace("AtCoder Beginner Contest ", "")
                         if x["title"].replace("AtCoder Beginner Contest ", "").isdigit() else 0))
    latest_problem = f"ABC{latest_abc['title'].replace('AtCoder Beginner Contest ', '')}"
    print(f"Latest ABC contest: {latest_problem}")

    # Process problem data
    print("\nProcessing problem data...")
    difficulty_distribution = {}

    # Use a fixed mapping for ABC problem indices to standard point values
    abc_index_to_points = {
        "A": 100,
        "B": 200,
        "C": 300,
        "D": 400,
        "E": 500,
        "F": 600,
        "G": 700,
        "H": 800,
        "Ex": 800
    }

    for problem_id, problem_info in problems.items():
        if problem_id.startswith("abc"):
            # For ABC problems, use the standard point values based on problem index
            problem_index = problem_info.get("problem_index", "")
            point_value = abc_index_to_points.get(problem_index, 0)

            # Get merged problem data if available for more accurate point value
            if problem_id in merged_problems and merged_problems[problem_id].get("point") is not None:
                point_value = int(merged_problems[problem_id]["point"])

            # Determine color based on difficulty ranges
            if point_value < 400:
                color = "grey"
            elif point_value < 800:
                color = "brown"
            elif point_value < 1200:
                color = "green"
            elif point_value < 1600:
                color = "cyan"
            elif point_value < 2000:
                color = "blue"
            elif point_value < 2400:
                color = "yellow"
            elif point_value < 2800:
                color = "orange"
            else:
                color = "red"

            print(f"Problem: {problem_id}, Index: {problem_index}, Point Value: {point_value}, Color: {color}")

            # Track difficulty distribution
            if color not in difficulty_distribution:
                difficulty_distribution[color] = 0
            difficulty_distribution[color] += 1

            update_statics(point_value, color, statics)

    # Debug: Print difficulty distribution
    print("\nDifficulty distribution:")
    for color, count in sorted(difficulty_distribution.items()):
        print(f"{color}: {count} problems")

    print("\nStatistics generated successfully")
except Exception as e:
    print(f"Error fetching data from API: {e}")

# Calculate summary statistics
total_solved = sum(sum(v.values()) for v in statics.values())
total_possible = 0
for diff, color_counts in statics.items():
    total_possible += sum(color_counts.values())
solve_rate = (
    round((total_solved / total_possible) * 100, 2) if total_possible > 0 else 0
)

# Generate table rows HTML
table_rows = ""
for diff, color_counts in sorted(statics.items()):
    total_count = sum(color_counts.values()) if sum(color_counts.values()) > 0 else 1
    table_rows += f"            <tr>\n"
    table_rows += f"                <td class='difficulty-label'>{diff}</td>\n"
    for color in colors:
        count = color_counts.get(color, 0)
        percentage = round((count / total_count) * 100, 2)
        circle_color_class = f"color-{color}" if count > 0 else "empty-color"
        bg_color_class = f"bg-{color}" if count > 0 else ""
        table_rows += f"                <td>\n"
        table_rows += f"                    <div class='stats-container'>\n"
        table_rows += f"                        <div class='circle-container'>\n"
        table_rows += f"                            <div class='progress-circle {circle_color_class}' data-color='var(--{color})' data-percent='{percentage}'>\n"
        table_rows += f"                                <span class='progress-circle-inner {bg_color_class}'></span>\n"
        table_rows += f"                            </div>\n"
        table_rows += f"                            <span class='count {circle_color_class}'>{count}</span>\n"
        table_rows += "                        </div>\n"
        table_rows += f"                        <span class='percentage {circle_color_class}'>({percentage}%)</span>\n"
        table_rows += "                    </div>\n"
        table_rows += "                </td>\n"
    table_rows += "            </tr>\n"

# Read the template file
with open("web-page/template.html", "r") as template_file:
    template = template_file.read()

# Replace placeholders with actual content
html_content = template.format(
    latest_problem=latest_problem,
    table_rows=table_rows
)

# Write the final HTML
with open("web-page/index.html", "w") as file:
    file.write(html_content)