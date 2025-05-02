# AtCoder Statistics

This project fetches difficulty statistics for AtCoder Beginner Contest (ABC) problems from the [AtCoder Problems API](https://kenkoooo.com/atcoder/#/api) and generates a simple HTML page visualizing the distribution of problems by difficulty and color rating.

## Features

- **API Integration:** Uses direct API calls to fetch problem statistics from the AtCoder Problems API.
- **Visualizes Data:** Generates an HTML table with color-coded progress circles to represent the percentage of problems at each difficulty level for each color rating (Grey, Brown, Green, Cyan, Blue, Yellow, Orange, Red).
- **Responsive Design:** The generated HTML table is responsive and adapts to different screen sizes.
- **Dynamic Progress Circles:** Uses JavaScript to dynamically generate progress circles based on problem statistics.
- **PR Previews:** Automatically generates preview deployments for pull requests.

## Requirements

- Python 3.6+
- requests

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

## Usage

1.  Clone the repository:

    ```bash
    git clone git@github.com:wulukewu/atcoder-statistics.git
    cd atcoder-statistics
    ```

2.  Run the `main.py` script:

    ```bash
    python main.py
    ```

    This script will:

    - Fetch data from the AtCoder Problems API
    - Process the problem statistics
    - Generate an `index.html` file in the `web-page/` directory.

3.  Open the `web-page/index.html` file in your browser to view the visualized data.

## File Structure

```
atcoder-statistics/
├── main.py            # Python script to fetch data and generate HTML
├── web-page/          # Directory for web page files
│   ├── index.html       # Generated HTML file with the table and visualization
│   ├── template.html    # HTML template for generating the final page
│   └── style.css        # CSS file for styling the HTML page
├── requirements.txt   # List of Python dependencies
└── README.md          # This file
```

## Example Output

The generated HTML page displays a table similar to this:

| Score      | Grey       | Brown  | Green  | Cyan   | Blue   | Yellow | Orange | Red    |
| :--------- | :--------- | :----- | :----- | :----- | :----- | :----- | :----- | :----- |
| 100        | 331 (100%) | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| 150        | 20 (100%)  | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| ...        | ...        | ...    | ...    | ...    | ...    | ...    | ...    | ...    |

Each cell in the table contains a progress circle visually representing the percentage, along with the raw count and percentage value.

## Contributing

We welcome contributions! Here's how you can help:

1. **Fork the Repository:**

   - Click the "Fork" button on the top right of this repository
   - Clone your fork to your local machine

2. **Create a Branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes:**

   - Make your changes
   - Test your changes locally
   - Commit your changes with clear commit messages

4. **Create a Pull Request:**

   - Push your branch to your fork
   - Create a Pull Request (PR) to the main repository
   - For work in progress, create a Draft PR:
     - Click "Create Pull Request"
     - Click the dropdown arrow next to "Create Pull Request"
     - Select "Create Draft Pull Request"
   - Once ready for review, click "Ready for review" on your Draft PR

5. **PR Preview:**

   - Each PR automatically gets a preview deployment
   - The preview URL will be posted as a comment on your PR
   - Preview URL format: `https://<username>.github.io/atcoder-statistics/pr-preview/pr-<number>/`
   - Use the preview to verify your changes before requesting review

6. **Code Review:**
   - Address any feedback from reviewers
   - Make additional commits if needed
   - Once approved, your PR will be merged

## Customization

- **Styling:** Modify the `web-page/style.css` file to customize the appearance of the HTML page.
- **Data Source:** The script currently fetches data from the AtCoder Problems API. You can modify the API endpoints in `main.py` if needed.
- **Colors:** The colors for each difficulty are defined in the `color_codes` dictionary within the `main.py` file. Modify these values to use different colors.

## Troubleshooting

- **API Issues:** If you encounter issues with the API, check if the endpoints are still valid and accessible.
- **Data Processing:** If the data structure from the API changes, you may need to update the data processing logic in `main.py`.

## License

This project is licensed under the terms of the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
