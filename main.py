import json
import os

# Load chart data from chart.json
with open('web-page/json/chart.json', 'r', encoding='utf-8') as f:
    chart = json.load(f)

# Initialize variables to store contest statistics
latest_contest_abc = None
colors = ['grey', 'brown', 'green', 'cyan', 'blue', 'yellow', 'orange', 'red']

# Process ABC contest statistics specifically
abc_statics = {}
for point, color_counts in chart['abc'].items():
    total_count = sum(color_counts.values()) if sum(color_counts.values()) > 0 else 1
    for color, count in color_counts.items():
        if point not in abc_statics:
            abc_statics[point] = {}
        if color not in abc_statics[point]:
            abc_statics[point][color] = 0
        abc_statics[point][color] += count

# Generate HTML table rows for the statistics
table_rows = ""
for point, color_counts in sorted(abc_statics.items()):
    total_count = sum(color_counts.values()) if sum(color_counts.values()) > 0 else 1
    table_rows += f"            <tr>\n"
    table_rows += f"                <td class='difficulty-label'>{int(float(point))}</td>\n"
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
    latest_contest_abc="N/A",  # Replace with actual logic if needed
    table_rows=table_rows
)

# Write the final HTML file
with open('web-page/index.html', 'w') as file:
    file.write(html_content)

print('[INFO] Successfully generated web page')