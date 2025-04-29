import requests
import json
import math
import time

def update_statics(diff, color, statics):
    if diff in statics:
        if color in statics[diff]:
            statics[diff][color] += 1
        else:
            statics[diff][color] = 1
    else:
        statics[diff] = {}
        statics[diff][color] = 1


def clip_difficulty(difficulty):
    """
    Clips the difficulty value using the same algorithm as in the frontend code.
    """
    if difficulty >= 400:
        return round(difficulty)
    else:
        return round(400 / math.exp(1.0 - difficulty / 400))


def get_rating_color(rating):
    """
    Returns the color name based on the rating value.
    Uses the exact same logic as AtCoder Problems frontend.
    """
    # Note: index 0 is "Black" in the original code, but we're using lowercase names
    # and our array starts with "grey" at index 0
    if rating < 400:
        return "grey"
    elif rating < 800:
        return "brown"
    elif rating < 1200:
        return "green"
    elif rating < 1600:
        return "cyan"
    elif rating < 2000:
        return "blue"
    elif rating < 2400:
        return "yellow"
    elif rating < 2800:
        return "orange"
    else:
        return "red"


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

# Fetch data from the API
print("Fetching problem models with difficulty ratings...")
models_response = requests.get("https://kenkoooo.com/atcoder/resources/problem-models.json")
problem_models = models_response.json()
print(f"Found {len(problem_models)} problem models")

# Debug: Print a few sample problems with their raw difficulties
print("\nSample problem difficulties (raw):")
sample_count = 0
for problem_id, model in list(problem_models.items())[:10]:
    if "difficulty" in model:
        print(f"Problem ID: {problem_id}, Raw Difficulty: {model['difficulty']}")
        sample_count += 1
    if sample_count >= 5:
        break

# Also fetch contest information to identify ABC contests
print("\nFetching contest information...")
contests_response = requests.get("https://kenkoooo.com/atcoder/resources/contests.json")
contests = contests_response.json()

# Find the latest ABC contest
abc_contests = [contest for contest in contests if contest["title"].startswith("AtCoder Beginner Contest")]
latest_abc = max(abc_contests, key=lambda x: int(x["title"].replace("AtCoder Beginner Contest ", "")
                     if x["title"].replace("AtCoder Beginner Contest ", "").isdigit() else 0))
latest_problem = f"ABC{latest_abc['title'].replace('AtCoder Beginner Contest ', '')}"
print(f"Latest ABC contest: {latest_problem}")

# Process problem data
print("\nProcessing problem data...")
difficulty_distribution = {}
for problem_id, model in problem_models.items():
    if "difficulty" in model:
        raw_difficulty = model["difficulty"]
        clipped_difficulty = clip_difficulty(raw_difficulty)
        color = get_rating_color(clipped_difficulty)

        # Track difficulty distribution for debugging
        if color not in difficulty_distribution:
            difficulty_distribution[color] = 0
        difficulty_distribution[color] += 1

        update_statics(clipped_difficulty, color, statics)

# Debug: Print difficulty distribution
print("\nDifficulty distribution:")
for color, count in difficulty_distribution.items():
    print(f"{color}: {count} problems")

# Debug: Print statistics structure
print("\nStatistics structure:")
for diff, color_counts in sorted(statics.items())[:10]:  # Show first 10 entries
    print(f"Difficulty {diff}: {color_counts}")

print("\nStatistics generated successfully")

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