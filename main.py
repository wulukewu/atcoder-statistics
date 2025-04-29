import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


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
)

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
    <link rel="stylesheet" href="styles.css">
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
                <div class="table-responsive">
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
        bg_color_class = f"bg-{color}" if count > 0 else ""
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
    </div>
    <div class="floating-button" onclick="window.open('https://kenkoooo.com/atcoder/#/table', '_blank');">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" width="24" height="24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
        </svg>
    </div>
    <div class="theme-toggle" onclick="toggleTheme()">
        <svg class="sun-icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
        </svg>
        <svg class="moon-icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
        </svg>
    </div>
    <div class="color-theme-toggle" onclick="cycleThemeColor()">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" width="24" height="24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h.01" />
        </svg>
    </div>
    <script src="script.js"></script>
</body>
</html>
"""
with open("web-page/index.html", "w") as file:
    file.write(html_content)