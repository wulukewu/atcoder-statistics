import time
import requests

latest_problem = None
statics = {
    'abc': {},
    'arc': {},
    'agc': {},
    'other': {}
}
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

contest_problems = requests.get("https://kenkoooo.com/atcoder/resources/contest-problem.json").json()
# print('contest_problems', contest_problems)
problem_models = requests.get("https://kenkoooo.com/atcoder/resources/problem-models.json").json()
# print('problem_models', problem_models)
merged_problems = requests.get("https://kenkoooo.com/atcoder/resources/merged-problems.json").json()
# print('merged_problems', merged_problems)

for problem in contest_problems:
    print(f'problem: {problem}')
    if 'abc' in problem['contest_id']:
        if problem['contest_id'] not in statics['abc']:
            statics['abc'][problem['contest_id']] = {}
        if problem['problem_id'] not in statics['abc'][problem['contest_id']]:
            statics['abc'][problem['contest_id']][problem['problem_id']] = {
                'problem_index': problem['problem_index'],
            }
    elif 'arc' in problem['contest_id']:
        if problem['contest_id'] not in statics['arc']:
            statics['arc'][problem['contest_id']] = {}
        if problem['problem_id'] not in statics['arc'][problem['contest_id']]:
            statics['arc'][problem['contest_id']][problem['problem_id']] = {
                'problem_index': problem['problem_index'],
            }
    elif 'agc' in problem['contest_id']:
        if problem['contest_id'] not in statics['agc']:
            statics['agc'][problem['contest_id']] = {}
        if problem['problem_id'] not in statics['agc'][problem['contest_id']]:
            statics['agc'][problem['contest_id']][problem['problem_id']] = {
                'problem_index': problem['problem_index'],
            }
    else:
        if problem['contest_id'] not in statics['other']:
            statics['other'][problem['contest_id']] = {}
        if problem['problem_id'] not in statics['other'][problem['contest_id']]:
            statics['other'][problem['contest_id']][problem['problem_id']] = {
                'problem_index': problem['problem_index'],
            }

print(statics)

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