import json
import os

# Load chart and stats data from JSON files
with open('web-page/json/chart.json', 'r', encoding='utf-8') as f:
    chart = json.load(f)
print(f"Loaded chart with {len(chart['abc'])} ABC point entries")
with open('web-page/json/stats.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)
print(f"Loaded stats for {len(stats['abc'])} ABC contests")
with open('web-page/json/problem_dict.json', 'r', encoding='utf-8') as f:
    problem_dict = json.load(f)
print(f"Loaded problem_dict with {len(problem_dict['abc'])} ABC point entries")

# Define color order for table columns
COLOR_ORDER = ['grey', 'brown', 'green', 'cyan', 'blue', 'yellow', 'orange', 'red']

# Aggregate ABC contest statistics by point and color
abc_stats = {}
for point, color_counts in chart['abc'].items():
    if point not in abc_stats:
        abc_stats[point] = {color: 0 for color in COLOR_ORDER}
    for color, count in color_counts.items():
        abc_stats[point][color] += count

def generate_problem_list_pages(problem_dict, stats, output_dir='web-page'):
    """Generate a separate HTML page for each (point, color) box listing the problems."""
    os.makedirs(f'{output_dir}/lists', exist_ok=True)
    # Read the list template from file
    with open(f'{output_dir}/template-list.html', 'r', encoding='utf-8') as f:
        template = f.read()
    for point, color_dict in problem_dict['abc'].items():
        for color, problem_ids in color_dict.items():
            items = []
            for pid in problem_ids:
                # Find contest_id for this problem_id
                contest_id = None
                name = pid
                for cid, problems in stats['abc'].items():
                    if pid in problems:
                        contest_id = cid
                        name = problems[pid].get('name', pid)
                        break
                if contest_id:
                    url = f"https://atcoder.jp/contests/{contest_id}/tasks/{pid}"
                    items.append(f'<li><a href="{url}" target="_blank">{name}</a> <span style="color:var(--{color})">[{pid}]</span></li>')
                else:
                    items.append(f'<li>{name} <span style="color:var(--{color})">[{pid}]</span></li>')
            problem_list = '\n                    '.join(items)
            html = template.format(point=point, color=color, problem_list=problem_list)
            filename = f'{output_dir}/lists/abc_{point}_{color}.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
    print('[INFO] Problem list pages generated.')

def render_table_rows(stats_by_point):
    """Generate HTML table rows for ABC statistics, with links to problem lists."""
    rows = ""
    for point, color_counts in sorted(stats_by_point.items(), key=lambda x: float(x[0])):
        total = sum(color_counts.values()) or 1
        rows += f"            <tr>\n"
        rows += f"                <td class='score-label'>{int(float(point))}</td>\n"
        for color in COLOR_ORDER:
            count = color_counts.get(color, 0)
            percent = round((count / total) * 100, 2)
            circle_class = f"color-{color}" if count > 0 else "empty-color"
            bg_class = f"bg-{color}" if count > 0 else ""
            # Link to list page if count > 0
            if count > 0:
                link = f"<a href='lists/abc_{point}_{color}.html' class='box-link'>"
                link_end = "</a>"
            else:
                link = ""
                link_end = ""
            rows += (
                f"                <td>\n"
                f"                    {link}<div class='stats-container'>\n"
                f"                        <div class='circle-container'>\n"
                f"                            <div class='progress-circle {circle_class}' data-color='var(--{color})' data-percent='{percent}'>\n"
                f"                                <span class='progress-circle-inner {bg_class}'></span>\n"
                f"                            </div>\n"
                f"                            <span class='count {circle_class}'>{count}</span>\n"
                f"                        </div>\n"
                f"                        <span class='percentage {circle_class}'>({percent}%)</span>\n"
                f"                    </div>{link_end}\n"
                f"                </td>\n"
            )
        rows += "            </tr>\n"
    return rows

table_rows = render_table_rows(abc_stats)

# Read the HTML template
with open('web-page/template.html', 'r') as template_file:
    template = template_file.read()

# Find the latest ABC contest with at least one colored problem
print("Searching for latest ABC contest with colored problems...")
latest_contest_abc = "N/A"
for contest_id in reversed(stats['abc']):
    if any(problem.get("color") and problem.get("point") for problem in stats['abc'][contest_id].values()):
        latest_contest_abc = contest_id
        break

# Fill the template with generated content
html_content = template.format(
    latest_contest_abc=latest_contest_abc.upper(),
    table_rows=table_rows
)

# Write the final HTML file
with open('web-page/index.html', 'w') as file:
    file.write(html_content)

print('[INFO] Successfully generated web page')

generate_problem_list_pages(problem_dict, stats)

