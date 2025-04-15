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
        WebDriverWait(driver, 5).until(lambda d: d.find_element(By.XPATH, '//*[@id="task-statement"]/span/span[2]/p/var/span/span/span[2]'))
        score = driver.find_element(By.XPATH, '//*[@id="task-statement"]/span/span[2]/p/var/span/span/span[2]')
        diff = int(score.text)
        # print(problem, diff, color)
        update_statics(diff, color, statics)
    except Exception as e:
        print(f'Error to get score from {link}')
        return

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')

driver = webdriver.Chrome(options=options)

driver.get('https://kenkoooo.com/atcoder/#/table')

latest_problem = None
statics = {}
colors = ['grey', 'brown', 'green', 'cyan', 'blue', 'yellow', 'orange', 'red']
color_codes = {
    'grey': '#8e44ad',
    'brown': 'rgb(128, 64, 0)',
    'green': 'rgb(0, 128, 0)',
    'cyan': 'rgb(0, 192, 192)',
    'blue': 'rgb(0, 0, 255)',
    'yellow': 'rgb(192, 192, 0)',
    'orange': 'rgb(255, 128, 0)',
    'red': 'rgb(255, 0, 0)'
}
problem_links = []

try:
    time.sleep(5)
    table = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div[1]/div[2]/table/tbody')
    for row in table.find_elements(By.TAG_NAME, 'tr'):
        idx = 0
        contest_problem_count = 0
        for cell in row.find_elements(By.TAG_NAME, 'td'):
            try:
                if idx == 0:
                    problem = cell.text.split(' ')[1]
                    # print(problem)
                else:
                    try:
                        diff = cell.find_element(By.CLASS_NAME, 'table-problem-point').text
                        diff = int(diff)
                    except:
                        diff = -1
                    
                    try:
                        problem_tmp = cell.find_element(By.TAG_NAME, 'a')
                        problem_link = problem_tmp.get_attribute('href')
                        color = problem_tmp.get_attribute('class')
                        color = color.split('difficulty-')[1]
                    except:
                        color = None
                    # print(diff, color)

                    if color is None:
                        continue
                    elif diff == -1:
                        contest_problem_count += 1
                        try:
                            if int(problem.replace('ABC', '')) > 41:
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
                    elif int(problem.replace('ABC', '')) > int(latest_problem.replace('ABC', '')):
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

# Generate HTML
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="favicon.svg" type="image/x-icon">
    <title>AtCoder Beginner Contest</title>
    <link rel="stylesheet" href="style.css">
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f7fa;
        }}
        h1, h2 {{
            color: #333;
            text-align: center;
        }}
        h1 {{
            margin-bottom: 10px;
            color: #2c3e50;
        }}
        h2 {{
            margin-bottom: 30px;
            color: #3498db;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 30px 0;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
        }}
        th, td {{
            padding: 15px;
            text-align: center;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #3498db;
            color: white;
            font-weight: 600;
        }}
        tr:hover {{
            background-color: #f1f1f1;
        }}
        .progress-circle {{
            position: relative;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            border: 5px solid;
            margin: 0 auto 10px;
        }}
        .progress-circle-inner {{
            position: absolute;
            top: 5px;
            left: 5px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: white;
        }}
        .floating-button {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background-color: #3498db;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        .floating-button:hover {{
            transform: scale(1.1);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }}
        .floating-button img {{
            width: 40px;
            height: 40px;
            object-fit: contain;
        }}
    </style>
</head>
<body>
    <h1>AtCoder Beginner Contest</h1>
    <h2>Latest Problem: {latest_problem}</h2>
    <table>
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
    total_count = sum(color_counts.values())
    html_content += f"            <tr>\n"
    html_content += f"                <td>{diff}</td>\n"
    for color in colors:
        count = color_counts.get(color, 0)
        percentage = (count / total_count * 100) if total_count > 0 else 0
        # Get the color code from the dictionary
        circle_color = color_codes.get(color, "grey")  # Default to grey if not found
        text_color = color_codes.get(color, '#c8c8c8')  # if percentage == 0 else ''  # Default to light grey if 0%, otherwise use CSS color
        # text_color = '#c8c8c8' if percentage == 0 else ''
        border_color = color_codes.get(color, '#c8c8c8') #if percentage == 0 else circle_color
        # border_color = '#c8c8c8' if percentage == 0 else circle_color
        # Use grey color if the percentage is 0, otherwise use the difficulty color
        html_content += f"                <td>\n"
        html_content += f"                    <div class='progress-circle' style='border-color: {border_color};' data-color='{circle_color}' data-percent='{percentage:.2f}'>\n"  # Use final_circle_color
        html_content += f"                        <span class='progress-circle-inner'></span>\n"
        html_content += f"                    </div>\n"
        html_content += f"                    <span style='color: {text_color};'>{count}</span>\n"
        html_content += f"                    <br>\n"
        html_content += f"                    <span style='color: {text_color};'>({percentage:.2f}%)</span>\n"
        html_content += "                </td>\n"
    html_content += "            </tr>\n"
html_content += """
        </tbody>
    </table>
    <div class="floating-button" onclick="window.open('https://kenkoooo.com/atcoder/#/table', '_blank');">
        <img src="atcoder-problems-logo.png" alt="AtCoder Problems">
    </div>
    <script>
        // You could add JavaScript here to make the progress circles dynamic
        // For example, to fill the circles based on the data-percent attribute
        document.addEventListener('DOMContentLoaded', function() {
            // This would be where you'd add code to animate the progress circles
        });
    </script>
</body>
</html>
"""

# Write to HTML file
with open("web-page/index.html", "w") as file:
    file.write(html_content)