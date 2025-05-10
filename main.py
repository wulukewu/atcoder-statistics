import json
import os

# Load chart and stats data from JSON files
with open('web-page/json/chart.json', 'r', encoding='utf-8') as f:
    chart = json.load(f)
print(f"Loaded chart with {len(chart['abc'])} ABC point entries")
with open('web-page/json/stats.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)
print(f"Loaded stats for {len(stats['abc'])} ABC contests")

# Define color order for table columns
COLOR_ORDER = ['grey', 'brown', 'green', 'cyan', 'blue', 'yellow', 'orange', 'red']

# Aggregate ABC contest statistics by point and color
abc_stats = {}
for point, color_counts in chart['abc'].items():
    if point not in abc_stats:
        abc_stats[point] = {color: 0 for color in COLOR_ORDER}
    for color, count in color_counts.items():
        abc_stats[point][color] += count

def render_table_rows(stats_by_point):
    """Generate HTML table rows for ABC statistics."""
    rows = ""
    for point, color_counts in sorted(stats_by_point.items(), key=lambda x: float(x[0])):
        print(f"Generating row for point: {point}, color counts: {color_counts}")
        total = sum(color_counts.values()) or 1
        rows += f"            <tr>\n"
        rows += f"                <td class='score-label'>{int(float(point))}</td>\n"
        for color in COLOR_ORDER:
            count = color_counts.get(color, 0)
            percent = round((count / total) * 100, 2)
            circle_class = f"color-{color}" if count > 0 else "empty-color"
            bg_class = f"bg-{color}" if count > 0 else ""
            rows += (
                f"                <td>\n"
                f"                    <div class='stats-container'>\n"
                f"                        <div class='circle-container'>\n"
                f"                            <div class='progress-circle {circle_class}' data-color='var(--{color})' data-percent='{percent}'>\n"
                f"                                <span class='progress-circle-inner {bg_class}'></span>\n"
                f"                            </div>\n"
                f"                            <span class='count {circle_class}'>{count}</span>\n"
                f"                        </div>\n"
                f"                        <span class='percentage {circle_class}'>({percent}%)</span>\n"
                f"                    </div>\n"
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
