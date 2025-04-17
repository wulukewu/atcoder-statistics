import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def update_statics(diff, color, statics):
    if diff in statics:
        if color in statics[diff]:
            statics[diff][color] += 1
        else:
            statics[diff][color] = 1
    else:
        statics[diff] = {}
        statics[diff][color] = 1


def process_problem_link(driver, link, color, statics):
    driver.get(link)
    try:
        WebDriverWait(driver, 5).until(
            lambda d: d.find_element(
                By.XPATH,
                '//*[@id="task-statement"]/span/span[2]/p/var/span/span/span[2]',
            )
        )
        score = driver.find_element(
            By.XPATH,
            '//*[@id="task-statement"]/span/span[2]/p/var/span/span/span[2]',
        )
        diff = int(score.text)
        # print(problem, diff, color)
        update_statics(diff, color, statics)
    except Exception as e:
        print(f"Error to get score from {link}")
        return


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-insecure-localhost")
driver = webdriver.Chrome(options=options)
driver.get("https://kenkoooo.com/atcoder/#/table")
latest_problem = None
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
problem_links = []
try:
    time.sleep(5)
    table = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div[1]/div[2]/table/tbody'
    )
    for row in table.find_elements(By.TAG_NAME, "tr"):
        idx = 0
        contest_problem_count = 0
        for cell in row.find_elements(By.TAG_NAME, "td"):
            try:
                if idx == 0:
                    problem = cell.text.split(" ")[1]
                    # print(problem)
                else:
                    try:
                        diff = cell.find_element(
                            By.CLASS_NAME, "table-problem-point"
                        ).text
                        diff = int(diff)
                    except:
                        diff = -1

                    try:
                        problem_tmp = cell.find_element(By.TAG_NAME, "a")
                        problem_link = problem_tmp.get_attribute("href")
                        color = problem_tmp.get_attribute("class")
                        color = color.split("difficulty-")[1]
                    except:
                        color = None
                    # print(diff, color)
                    if color is None:
                        continue
                    elif diff == -1:
                        contest_problem_count += 1
                        try:
                            if int(problem.replace("ABC", "")) > 41:
                                # print(problem_link)
                                problem_links.append([problem, problem_link, color])
                        except Exception as e:
                            continue
                    else:
                        contest_problem_count += 1
                        update_statics(diff, color, statics)
                if contest_problem_count >= 4:
                    if latest_problem is None:
                        latest_problem = problem
                    elif int(problem.replace("ABC", "")) > int(
                        latest_problem.replace("ABC", "")
                    ):
                        latest_problem = problem
                    # print(f'Latest Problem: {latest_problem}')
            except Exception as e:
                pass
            idx += 1
    # print(problem_links)
    for problem, link, color in problem_links:
        process_problem_link(driver, link, color, statics)
    print(statics)
except Exception as e:
    print(e)
driver.quit()

# Calculate summary statistics
total_solved = sum(sum(v.values()) for v in statics.values())
total_possible = 0
for diff, color_counts in statics.items():
    total_possible += sum(color_counts.values())
solve_rate = (
    round((total_solved / total_possible) * 100, 2) if total_possible > 0 else 0
)  # Success Rate - replace with actual logic if possible
Rating = 1245  # Replace with actual logic if scraping rating
contests = 28  # Replace with actual logic if scraping contests


# Generate HTML
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AtCoder Statistics Dashboard</title>
    <link rel="icon" href="favicon.svg" type="image/x-icon">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #10b981; /* Changed from indigo to emerald green */
            --primary-dark: #059669; /* Darker green */
            --primary-light: #a7f3d0; /* Lighter green */
            --gray-50: #f9fafb;
            --gray-100: #f3f4f6;
            --gray-200: #e5e7eb;
            --gray-300: #d1d5db;
            --gray-400: #9ca3af;
            --gray-500: #6b7280;
            --gray-600: #4b5563;
            --gray-700: #374151;
            --gray-800: #1f2937;
            --gray-900: #111827;
            --red: #ef4444;
            --orange: #f97316;
            --yellow: #eab308;
            --green: #22c55e;
            --cyan: #06b6d4;
            --blue: #3b82f6;
            --purple: #8b5cf6;
            --brown: #a16207;
        }}
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #f9fafb;
            color: var(--gray-800);
            line-height: 1.5;
            padding: 0;
            margin: 0;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
        }}
        header {{
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: white;
            padding: 2rem 0;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            position: relative;
            overflow: hidden;
        }}
        .header-content {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            position: relative;
            z-index: 2;
        }}
        .header-bg {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            opacity: 0.1;
        }}
        .header-bg-circle {{
            position: absolute;
            border-radius: 50%;
            background: white;
        }}
        .circle-1 {{
            width: 300px;
            height: 300px;
            top: -150px;
            left: -100px;
        }}
        .circle-2 {{
            width: 200px;
            height: 200px;
            bottom: -100px;
            right: -50px;
        }}
        h1 {{
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }}
        h2 {{
            font-size: 1.5rem;
            font-weight: 500;
            opacity: 0.9;
        }}
        .dashboard-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}
        @media (max-width: 768px) {{
            .dashboard-grid {{
                grid-template-columns: 1fr;
            }}
        }}
        .card {{
            background-color: white;
            border-radius: 0.75rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            overflow: hidden;
            margin-bottom: 2rem;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }}
        .card-header {{
            padding: 1.25rem 1.5rem;
            border-bottom: 1px solid var(--gray-200);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .card-title {{
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--gray-900);
        }}
        .card-body {{
            padding: 1.5rem;
        }}
        .stats-table {{
            width: 100%;
            border-collapse: collapse;
        }}
        .stats-table th,
        .stats-table td {{
            padding: 1rem;
            text-align: center;
            border-bottom: 1px solid var(--gray-200);
        }}
        .stats-table th {{
            background-color: var(--gray-100);
            font-weight: 600;
            color: var(--gray-700);
            text-transform: uppercase;
            font-size: 0.75rem;
            letter-spacing: 0.05em;
        }}
        .stats-table tr:last-child td {{
            border-bottom: none;
        }}
        .stats-table tr:hover {{
            background-color: var(--gray-50);
        }}
        .difficulty-label {{
            font-weight: 600;
            color: var(--gray-700);
        }}
        .stats-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.25rem;
        }}
        .circle-container {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .progress-circle {{
            width: 16px;
            height: 16px;
            border-radius: 50%;
            border: 2px solid;
            position: relative;
            overflow: hidden;
        }}
        .progress-circle-inner {{
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 0%;
            border-radius: 0;
        }}
        .count {{
            font-weight: 600;
            font-size: 1rem;
        }}
        .percentage {{
            font-size: 0.875rem;
            opacity: 0.8;
        }}
        .floating-button {{
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            width: 3.5rem;
            height: 3.5rem;
            border-radius: 50%;
            background-color: var(--primary);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            cursor: pointer;
            transition: all 0.2s ease;
            z-index: 50;
        }}
        .floating-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            background-color: var(--primary-dark);
        }}
        .floating-button img {{
            width: 60%;
            height: 60%;
            object-fit: contain;
        }}
        .color-grey {{ color: var(--gray-500); border-color: var(--gray-500); }}
        .color-brown {{ color: var(--brown); border-color: var(--brown); }}
        .color-green {{ color: var(--green); border-color: var(--green); }}
        .color-cyan {{ color: var(--cyan); border-color: var(--cyan); }}
        .color-blue {{ color: var(--blue); border-color: var(--blue); }}
        .color-yellow {{ color: var(--yellow); border-color: var(--yellow); }}
        .color-orange {{ color: var(--orange); border-color: var(--orange); }}
        .color-red {{ color: var(--red); border-color: var(--red); }}
        .color-purple {{ color: var(--purple); border-color: var(--purple); }}
        .bg-grey {{ background-color: var(--gray-500); }}
        .bg-brown {{ background-color: var(--brown); }}
        .bg-green {{ background-color: var(--green); }}
        .bg-cyan {{ background-color: var(--cyan); }}
        .bg-blue {{ background-color: var(--blue); }}
        .bg-yellow {{ background-color: var(--yellow); }}
        .bg-orange {{ background-color: var(--orange); }}
        .bg-red {{ background-color: var(--red); }}
        .bg-purple {{ background-color: var(--purple); }}
        .empty-color {{ color: var(--gray-400); border-color: var(--gray-300); }}
        /* Tabs */
        .tabs {{
            display: flex;
            border-bottom: 1px solid var(--gray-200);
            margin-bottom: 1rem;
        }}
        .tab {{
            padding: 0.75rem 1.5rem;
            cursor: pointer;
            font-weight: 500;
            color: var(--gray-600);
            border-bottom: 2px solid transparent;
            transition: all 0.2s;
        }}
        .tab:hover {{
            color: var(--primary);
        }}
        .tab.active {{
            color: var(--primary);
            border-bottom-color: var(--primary);
        }}
        .tab-content {{
            display: none;
        }}
        .tab-content.active {{
            display: block;
        }}
    </style>
</head>
<body>
    <header>
        <div class="header-bg">
            <div class="header-bg-circle circle-1"></div>
            <div class="header-bg-circle circle-2"></div>
        </div>
        <div class="container header-content">
            <h1>AtCoder Statistics</h1>
            <h2>Latest Contest: {latest_problem}</h2>
        </div>
    </header>
    <div class="container">
        <!-- Main Content with Tabs -->
        <div class="card">
            <div class="card-header">
                <div class="card-title">AtCoder Problems</div>
            </div>
            <div class="tabs">
                <div class="tab active" data-tab="table">AtCoder Beginner Contest</div>
            </div>
            <div class="tab-content active" id="table-content">
                <table class="stats-table">
                    <thead>
                        <tr>
                            <th>Difficulty</th>
                            <th>Grey</th>
                            <th>Brown</th>
                            <th>Green</th>
                            <th>Cyan</th>
                            <th>Blue</th>
                            <th>Yellow</th>
                            <th>Orange</th>
                            <th>Red</th>
                        </tr>
                    </thead>
                    <tbody>
"""
for diff, color_counts in sorted(statics.items()):
    total_count = sum(color_counts.values()) if sum(color_counts.values()) > 0 else 1
    html_content += f"            <tr>\n"
    html_content += f"                <td class='difficulty-label'>{diff}</td>\n"
    for color in colors:
        count = color_counts.get(color, 0)
        percentage = round((count / total_count) * 100, 2)
        circle_color_class = f"color-{color}" if count > 0 else "empty-color"
        bg_color_class = f"bg-{color}" if count > 0 else ""  #No background if 0
        html_content += f"                <td>\n"
        html_content += f"                    <div class='stats-container'>\n"
        html_content += f"                        <div class='circle-container'>\n"
        html_content += f"                            <div class='progress-circle {circle_color_class}' data-color='var(--{color})' data-percent='{percentage}'>\n"
        html_content += f"                                <span class='progress-circle-inner {bg_color_class}'></span>\n"
        html_content += f"                            </div>\n"
        html_content += f"                            <span class='count {circle_color_class}'>{count}</span>\n"
        html_content += "                        </div>\n"
        html_content += f"                        <span class='percentage {circle_color_class}'>({percentage}%)</span>\n"
        html_content += "                    </div>\n"
        html_content += "                </td>\n"
    html_content += "            </tr>\n"
html_content += """
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <div class="floating-button" onclick="window.open('https://kenkoooo.com/atcoder/#/table', '_blank');">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" width="24" height="24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
        </svg>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            // Initialize progress circles
            const circles = document.querySelectorAll('.progress-circle');
            circles.forEach(circle => {{
                const percent = parseFloat(circle.getAttribute('data-percent'));
                const innerCircle = circle.querySelector('.progress-circle-inner');
                // Set the height based on the percentage (fill from bottom)
                innerCircle.style.height = percent + '%';
            }});
        }});
    </script>
</body>
</html>
"""
with open("web-page/index.html", "w") as file:
    file.write(html_content)