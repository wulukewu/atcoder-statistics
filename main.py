import time
import requests
import json
import os

# Initialize variables to store contest statistics and problem mappings
latest_contest_abc = None
statics = {
    'abc': {},  # Store ABC contest problems and their details
    'arc': {},  # Store ARC contest problems and their details
    'agc': {},  # Store AGC contest problems and their details
    'other': {} # Store other contest problems and their details
}
problem_id_to_contest_id = {}  # Map problem IDs to their contest IDs

# Define color scheme for difficulty levels
colors = ['grey', 'brown', 'green', 'cyan', 'blue', 'yellow', 'orange', 'red']
color_codes = {
    'grey': '#6b7280',   # --gray-500
    'brown': '#a16207',  # --brown
    'green': '#22c55e',  # --green
    'cyan': '#06b6d4',   # --cyan
    'blue': '#3b82f6',   # --blue
    'yellow': '#eab308', # --yellow
    'orange': '#f97316', # --orange
    'red': '#ef4444',    # --red
}

# Fetch contest data from AtCoder API
contest_problems = requests.get('https://kenkoooo.com/atcoder/resources/contest-problem.json').json()
# print('contest_problems', contest_problems)
problem_models = requests.get('https://kenkoooo.com/atcoder/resources/problem-models.json').json()
# print('problem_models', problem_models)
merged_problems = requests.get('https://kenkoooo.com/atcoder/resources/merged-problems.json').json()
# print('merged_problems', merged_problems)

# Process contest problems and organize them by contest type
for problem in contest_problems:
    # print(f'problem: {problem}')
    # Categorize problems based on contest type (ABC, ARC, AGC, or other)
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
    
    # Build problem ID to contest ID mapping
    if problem['problem_id'] not in problem_id_to_contest_id:
        problem_id_to_contest_id[problem['problem_id']] = [problem['contest_id']]
    else:
        problem_id_to_contest_id[problem['problem_id']].append(problem['contest_id'])

# Add difficulty information from problem models
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

# Add point information from merged problems
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

# print(statics)

# Process ABC contest statistics specifically
abc_statics = {}
for contest_id in statics['abc']:
    # print(f'contest_id: {contest_id}')
    if int(contest_id.replace('abc', '')) <= 41: continue  # Skip older contests

    contest_has_data = False

    # Process each problem in the contest
    for problem_id in statics['abc'][contest_id]:
        if 'difficulty' in statics['abc'][contest_id][problem_id] and 'point' in statics['abc'][contest_id][problem_id]:
            point = statics['abc'][contest_id][problem_id]['point']
            difficulty = statics['abc'][contest_id][problem_id]['difficulty']

            # print(f'    problem_id: {problem_id}')
            # print(f'        point: {point}')
            # print(f'        difficulty: {difficulty}')
            # print(f'        problem_index: {statics["abc"][contest_id][problem_id]["problem_index"]}')
            contest_has_data = True

            # Determine color based on difficulty
            if difficulty < 400: color = 'grey'
            elif difficulty < 800: color = 'brown'
            elif difficulty < 1200: color = 'green'
            elif difficulty < 1600: color = 'cyan'
            elif difficulty < 2000: color = 'blue'
            elif difficulty < 2400: color = 'yellow'
            elif difficulty < 2800: color = 'orange'
            else: color = 'red'

            # Assign the determined color to the problem based on its difficulty
            statics['abc'][contest_id][problem_id]['color'] = color

            # Update statistics for this point value and color
            if point not in abc_statics:
                abc_statics[point] = {}
            if color not in abc_statics[point]:
                abc_statics[point][color] = 0
            abc_statics[point][color] += 1

    # Update latest ABC contest ID
    if contest_has_data:
        if latest_contest_abc is None:
            latest_contest_abc = contest_id.upper()
        elif int(contest_id.replace('abc', '')) > int(latest_contest_abc.replace('ABC', '')):
            latest_contest_abc = contest_id.upper()

# Create directory for JSON output if it doesn't exist
os.makedirs('web-page/json', exist_ok=True)

# Save problem ID to contest ID mapping for debugging
with open('web-page/json/problem_id_to_contest_id.json', 'w', encoding='utf-8') as f:
    json.dump(problem_id_to_contest_id, f, ensure_ascii=False, indent=2)

# Save complete statistics for debugging
with open('web-page/json/statics.json', 'w', encoding='utf-8') as f:
    json.dump(statics, f, ensure_ascii=False, indent=2)

# Save ABC statistics for debugging
with open('web-page/json/abc_statics.json', 'w', encoding='utf-8') as f:
    json.dump(abc_statics, f, ensure_ascii=False, indent=2)

print(f'latest_contest_abc: {latest_contest_abc}')
print(f'abc_statics: {abc_statics}')

# Generate HTML table rows for the statistics
table_rows = ""
for point, color_counts in sorted(abc_statics.items()):
    total_count = sum(color_counts.values()) if sum(color_counts.values()) > 0 else 1
    table_rows += f"            <tr>\n"
    table_rows += f"                <td class='score-label'>{int(point)}</td>\n"
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

# Read the HTML template
with open('web-page/template.html', 'r') as template_file:
    template = template_file.read()

# Generate final HTML by replacing placeholders
html_content = template.format(
    latest_contest_abc=latest_contest_abc,
    table_rows=table_rows
)

# Write the final HTML file
with open('web-page/index.html', 'w') as file:
    file.write(html_content)

print('[INFO] Successfully generated web page')