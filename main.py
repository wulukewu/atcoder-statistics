import json
import os

print("\n=== AtCoder Statistics Web Page Generation ===")
print("Loading data from JSON files...")

# Load chart and stats data from JSON files
with open('web-page/json/chart.json', 'r', encoding='utf-8') as f:
    chart = json.load(f)
print(f"✓ Loaded chart data:")
for contest_type in ['abc', 'arc', 'agc']:
    print(f"  - {contest_type.upper()}: {len(chart[contest_type])} point entries")

with open('web-page/json/stats.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)
print(f"✓ Loaded contest statistics:")
for contest_type in ['abc', 'arc', 'agc']:
    print(f"  - {contest_type.upper()}: {len(stats[contest_type])} contests")

with open('web-page/json/problem_dict.json', 'r', encoding='utf-8') as f:
    problem_dict = json.load(f)
print(f"✓ Loaded problem dictionary:")
for contest_type in ['abc', 'arc', 'agc']:
    print(f"  - {contest_type.upper()}: {len(problem_dict[contest_type])} point entries")

# Define color order for table columns
COLOR_ORDER = ['grey', 'brown', 'green', 'cyan', 'blue', 'yellow', 'orange', 'red','bronze', 'silver', 'gold']

print("\nAggregating contest statistics...")
# Aggregate ABC contest statistics by point and color
abc_stats = {}
for point, color_counts in chart['abc'].items():
    if point not in abc_stats:
        abc_stats[point] = {color: 0 for color in COLOR_ORDER}
    for color, count in color_counts.items():
        abc_stats[point][color] += count

arc_stats = {}
for point, color_counts in chart['arc'].items():
    if point not in arc_stats:
        arc_stats[point] = {color: 0 for color in COLOR_ORDER}
    for color, count in color_counts.items():
        arc_stats[point][color] += count

agc_stats = {}
for point, color_counts in chart['agc'].items():
    if point not in agc_stats:
        agc_stats[point] = {color: 0 for color in COLOR_ORDER}
    for color, count in color_counts.items():
        agc_stats[point][color] += count

print("✓ Statistics aggregated for all contest types")

def generate_problem_list_pages(problem_dict, stats):
    """Generate HTML pages for each point/color combination with problem lists."""
    print("\nGenerating problem list pages...")
    os.makedirs('web-page/lists', exist_ok=True)

    for contest_type in problem_dict:
        for point in problem_dict[contest_type]:
            for color in problem_dict[contest_type][point]:
                # Sort problem IDs in descending order
                problem_ids = sorted(problem_dict[contest_type][point][color], reverse=True)

                # Create directory structure
                dir_path = f'web-page/lists/{contest_type}/{int(float(point))}/{color}'
                os.makedirs(dir_path, exist_ok=True)

                # Generate the HTML content for this list
                html_content = generate_problem_list_html(problem_ids, stats, contest_type, point, color)

                # Write the HTML file
                with open(f'{dir_path}/index.html', 'w') as file:
                    file.write(html_content)

    print(f"✓ Problem list pages generated")

def render_table_rows(stats_by_point, contest_type='abc'):
    """Generate HTML table rows for contest statistics, with links to problem lists."""
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
                link = f"<a href='lists/{contest_type}/{int(float(point))}/{color}/' class='box-link'>"
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

print("\nGenerating table rows for each contest type...")
# Generate table rows for each contest type
table_rows_abc = render_table_rows(abc_stats, 'abc')
table_rows_arc = render_table_rows(arc_stats, 'arc')
table_rows_agc = render_table_rows(agc_stats, 'agc')
print("✓ Table rows generated")

# Read the HTML template
with open('web-page/template.html', 'r') as template_file:
    template = template_file.read()

# Find the latest contest with at least one colored problem
print("\nFinding latest contests with colored problems...")
def find_latest_contest_with_colored_problems(contest_type, stats):
    for contest_id in reversed(stats[contest_type]):
        if any(problem.get("color") and problem.get("point") for problem in stats[contest_type][contest_id].values()):
            return contest_id
    return "N/A"

latest_contest_abc = find_latest_contest_with_colored_problems('abc', stats)
latest_contest_arc = find_latest_contest_with_colored_problems('arc', stats)
latest_contest_agc = find_latest_contest_with_colored_problems('agc', stats)
print(f"✓ Latest ABC contest: {latest_contest_abc.upper()}")
print(f"✓ Latest ARC contest: {latest_contest_arc.upper()}")
print(f"✓ Latest AGC contest: {latest_contest_agc.upper()}")

# Fill the template with generated content
print("\nGenerating main page...")
html_content = template.format(
    latest_contest_abc=latest_contest_abc.upper(),
    latest_contest_arc=latest_contest_arc.upper(),
    latest_contest_agc=latest_contest_agc.upper(),
    table_rows_abc=table_rows_abc,
    table_rows_arc=table_rows_arc,
    table_rows_agc=table_rows_agc
)

# Write the final HTML file
with open('web-page/index.html', 'w') as file:
    file.write(html_content)
print("✓ Main page generated")

generate_problem_list_pages(problem_dict, stats)

print("\n=== Web Page Generation Complete ===")
