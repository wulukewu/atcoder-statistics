import time
import requests
import json

latest_contest = None
statics = {
    'abc': {},
    'arc': {},
    'agc': {},
    'other': {}
}
problem_id_to_contest_id = {}
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
    # print(f'problem: {problem}')
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
    if problem['problem_id'] not in problem_id_to_contest_id:
        problem_id_to_contest_id[problem['problem_id']] = [problem['contest_id']]
    else:
        problem_id_to_contest_id[problem['problem_id']].append(problem['contest_id'])

# Save problem_id_to_contest_id to a JSON file for debugging
with open('debug_problem_id_to_contest_id.json', 'w', encoding='utf-8') as f:
    json.dump(problem_id_to_contest_id, f, ensure_ascii=False, indent=2)

for problem in problem_models:
    # print(f'problem: {problem}')
    # print(f'problem_models: {problem_models[problem]}')
    if 'difficulty' in problem_models[problem] and problem in problem_id_to_contest_id:
        for contest_id in problem_id_to_contest_id[problem]:
            if 'abc' in contest_id:
                if contest_id in statics['abc']:
                    statics['abc'][contest_id][problem]['difficulty'] = problem_models[problem]['difficulty']
                else:
                    statics['abc'][contest_id][problem] = {
                        'difficulty': problem_models[problem]['difficulty'],
                    }
            elif 'arc' in contest_id:
                if contest_id in statics['arc']:
                    statics['arc'][contest_id][problem]['difficulty'] = problem_models[problem]['difficulty']
                else:
                    statics['arc'][contest_id][problem] = {
                        'difficulty': problem_models[problem]['difficulty'],
                    }
            elif 'agc' in contest_id:
                if contest_id in statics['agc']:
                    statics['agc'][contest_id][problem]['difficulty'] = problem_models[problem]['difficulty']
                else:
                    statics['agc'][contest_id][problem] = {
                        'difficulty': problem_models[problem]['difficulty'],
                    }
            else:
                if contest_id in statics['other']:
                    statics['other'][contest_id][problem]['difficulty'] = problem_models[problem]['difficulty']
                else:
                    statics['other'][contest_id][problem] = {
                        'difficulty': problem_models[problem]['difficulty'],
                    }

for problem in merged_problems:
    # print(f'problem: {problem}')
    if problem['id'] in problem_id_to_contest_id:
        for contest_id in problem_id_to_contest_id[problem['id']]:
            if contest_id in statics['abc']:
                statics['abc'][contest_id][problem['id']]['point'] = problem['point']
            elif contest_id in statics['arc']:
                statics['arc'][contest_id][problem['id']]['point'] = problem['point']
            elif contest_id in statics['agc']:
                statics['agc'][contest_id][problem['id']]['point'] = problem['point']
            else:
                statics['other'][contest_id][problem['id']] = {
                    'point': problem['point'],
                }

# Save statics to a JSON file for debugging
with open('debug_statics.json', 'w', encoding='utf-8') as f:
    json.dump(statics, f, ensure_ascii=False, indent=2)

# print(statics)

for contest_id in statics['abc']:
    print(f'contest_id: {contest_id}')
    if int(contest_id.replace('abc', '')) <= 41: continue

    contest_has_data = False

    for problem_id in statics['abc'][contest_id]:
        if 'difficulty' in statics['abc'][contest_id][problem_id] and 'point' in statics['abc'][contest_id][problem_id]:
            print(f'    problem_id: {problem_id}')
            print(f'        point: {statics["abc"][contest_id][problem_id]["point"]}')
            print(f'        difficulty: {statics["abc"][contest_id][problem_id]["difficulty"]}')
            print(f'        problem_index: {statics["abc"][contest_id][problem_id]["problem_index"]}')
            contest_has_data = True
    
    if contest_has_data:
        if latest_contest is None:
            latest_contest = contest_id.upper()
        elif int(contest_id.replace('abc', '')) > int(latest_contest.replace('ABC', '')):
            latest_contest = contest_id.upper()

print(f'latest_contest: {latest_contest}')

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
    latest_contest=latest_contest,
    table_rows=table_rows
)

# Write the final HTML
with open("web-page/index.html", "w") as file:
    file.write(html_content)