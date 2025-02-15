import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

try:
    time.sleep(5)
    table = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div[1]/div[2]/table/tbody')
    for row in table.find_elements(By.TAG_NAME, 'tr'):
        idx = 0
        for cell in row.find_elements(By.TAG_NAME, 'td'):
            try:
                if idx == 0:
                    # print(cell.text)
                    latest_problem_tmp = cell.text.split(' ')[1]
                else:
                    diff = cell.find_element(By.CLASS_NAME, 'table-problem-point').text
                    diff = int(diff)
                    color = cell.find_element(By.TAG_NAME, 'a').get_attribute('class')
                    color = color.split('difficulty-')[1]
                    # print(diff, color)
                    if diff in statics:
                        if color in statics[diff]:
                            statics[diff][color] += 1
                        else:
                            statics[diff][color] = 1
                    else:
                        statics[diff] = {}
                        statics[diff][color] = 1
                if idx >= 4 and latest_problem is None:
                    latest_problem = latest_problem_tmp

            except Exception as e:
                pass
            idx += 1
    
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
    <title>AtCoder Table</title>
    <link rel="stylesheet" href="style.css">
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
        color_style = "rgb(192, 192, 192)" if count == 0 else ""
        html_content += f"                <td style='color:{color_style}'>{count} ({percentage:.2f}%)</td>\n"
    html_content += "            </tr>\n"

html_content += """
        </tbody>
    </table>
</body>
</html>
"""

# Write to HTML file
with open("web-page/index.html", "w") as file:
    file.write(html_content)