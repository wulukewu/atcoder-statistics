import requests
import json
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

try:
    # Fetch data from the API
    print("Fetching problem data from API...")
    response = requests.get("https://kenkoooo.com/atcoder/resources/problem-models.json")
    problem_data = response.json()
    
    # Also fetch contest information to identify ABC contests
    print("Fetching contest information...")
    contests_response = requests.get("https://kenkoooo.com/atcoder/resources/contests.json")
    contests = contests_response.json()
    
    # Find the latest ABC contest
    abc_contests = [contest for contest in contests if contest["title"].startswith("AtCoder Beginner Contest")]
    latest_abc = max(abc_contests, key=lambda x: int(x["title"].replace("AtCoder Beginner Contest ", "")) 
                     if x["title"].replace("AtCoder Beginner Contest ", "").isdigit() else 0)
    latest_problem = f"ABC{latest_abc['title'].replace('AtCoder Beginner Contest ', '')}"
    print(f"Latest ABC contest: {latest_problem}")
    
    # Process problem data
    print("Processing problem data...")
    for problem_id, problem_info in problem_data.items():
        if "difficulty" in problem_info:
            diff = problem_info["difficulty"]
            
            # Determine color based on difficulty
            color = None
            if diff < 400:
                color = "grey"
            elif diff < 800:
                color = "brown"
            elif diff < 1200:
                color = "green"
            elif diff < 1600:
                color = "cyan"
            elif diff < 2000:
                color = "blue"
            elif diff < 2400:
                color = "yellow"
            elif diff < 2800:
                color = "orange"
            else:
                color = "red"
                
            update_statics(diff, color, statics)
    
    print("Statistics generated successfully")
    print(statics)
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

print("HTML file generated successfully at web-page/index.html")