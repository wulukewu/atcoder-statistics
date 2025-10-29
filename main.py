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

print("\nBuilding reverse lookup index for problems...")
# Create reverse lookup: problem_id -> (contest_id, contest_type) for O(1) lookup
problem_to_contest = {}
for contest_type in ['abc', 'arc', 'agc']:
    for contest_id, problems in stats[contest_type].items():
        for problem_id in problems:
            problem_to_contest[problem_id] = (contest_id, contest_type)
print(f"✓ Built index for {len(problem_to_contest)} problems")

# Define color order for table columns
COLOR_ORDER = ['grey', 'brown', 'green', 'cyan', 'blue', 'yellow', 'orange', 'red', 'bronze', 'silver', 'gold']

print("\nAggregating contest statistics...")
# Aggregate contest statistics by point and color for all contest types
def aggregate_stats(chart_data):
    """Aggregate statistics from chart data, initializing all colors for each point."""
    stats = {}
    for point, color_counts in chart_data.items():
        stats[point] = {color: 0 for color in COLOR_ORDER}
        for color, count in color_counts.items():
            stats[point][color] += count
    return stats

abc_stats = aggregate_stats(chart['abc'])
arc_stats = aggregate_stats(chart['arc'])
agc_stats = aggregate_stats(chart['agc'])
print("✓ Statistics aggregated for all contest types")

def generate_problem_list_pages(problem_dict, stats, problem_to_contest, output_dir='web-page'):
    """Generate a separate HTML page for each (point, color) box listing the problems."""
    print("\nGenerating problem list pages...")
    with open(f'{output_dir}/template-list.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Process each contest type (ABC, ARC, AGC)
    for contest_type in ['abc', 'arc', 'agc']:
        print(f"\nProcessing {contest_type.upper()} problems...")
        page_count = 0
        for point, color_dict in problem_dict[contest_type].items():
            point_int = int(float(point))
            for color, problem_ids in color_dict.items():
                items = []
                problem_ids.sort(reverse=True)
                for pid in problem_ids:
                    # Use O(1) lookup instead of O(n) iteration
                    lookup_result = problem_to_contest.get(pid)
                    if lookup_result:
                        contest_id, _ = lookup_result
                        name = stats[contest_type][contest_id][pid].get('name', pid)
                    else:
                        contest_id = None
                        name = pid
                    
                    # Format problem tag as 'ABC400A' (contest id upper + problem suffix upper)
                    if contest_id and '_' in pid:
                        contest_tag = contest_id.upper() + pid.split('_')[-1].upper()
                    else:
                        contest_tag = pid.upper()
                    if contest_id:
                        url = f"https://atcoder.jp/contests/{contest_id}/tasks/{pid}"
                        # Card layout for each problem
                        items.append(f'''
                        <div class="problem-card">
                            <div class="problem-header">
                                <span class="problem-title">{name}</span>
                                <span class="problem-badge color-{color}">{color}</span>
                            </div>
                            <div class="problem-meta">
                                <span class="problem-id">{contest_tag}</span>
                                <a href="{url}" target="_blank" class="external-link">Open
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 3h7m0 0v7m0-7L10 14m-4 0h4v4"/></svg>
                                </a>
                            </div>
                        </div>
                        ''')
                    else:
                        items.append(f'''
                        <div class="problem-card">
                            <div class="problem-header">
                                <span class="problem-title">{name}</span>
                                <span class="problem-badge color-{color}">{color}</span>
                            </div>
                            <div class="problem-meta">
                                <span class="problem-id">{contest_tag}</span>
                            </div>
                        </div>
                        ''')
                problem_list = '\n'.join(items)
                html = template.format(
                    contest_type=contest_type.upper(),
                    point=point_int,
                    color=color,
                    problem_list=problem_list
                )
                folder_path = f'{output_dir}/lists/{contest_type}/{point_int}/{color}'
                os.makedirs(folder_path, exist_ok=True)
                filename = f'{folder_path}/index.html'
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(html)
                page_count += 1
        print(f"✓ Generated {page_count} pages for {contest_type.upper()}")

def render_table_rows(stats_by_point, contest_type='abc'):
    """Generate HTML table rows for contest statistics, with links to problem lists."""
    rows = []  # Use list for efficient concatenation
    for point, color_counts in sorted(stats_by_point.items(), key=lambda x: float(x[0])):
        total = sum(color_counts.values()) or 1
        rows.append("            <tr>\n")
        rows.append(f"                <td class='score-label'>{int(float(point))}</td>\n")
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
            rows.append(
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
        rows.append("            </tr>\n")
    return ''.join(rows)  # Join once at the end

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
    # Iterate in reverse and use early exit for better performance
    for contest_id in reversed(list(stats[contest_type].keys())):
        # Check if any problem has both color and point using any() for short-circuit evaluation
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

generate_problem_list_pages(problem_dict, stats, problem_to_contest)

print("\n=== Web Page Generation Complete ===")

