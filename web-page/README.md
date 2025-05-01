# AtCoder Statistics Dashboard

A beautiful, interactive dashboard that visualizes AtCoder problem statistics by difficulty level and color rating.

## Overview

This dashboard scrapes and analyzes AtCoder problem data to provide insights into the distribution of problems across different difficulty levels and color ratings. The visualization helps competitive programmers understand the problem landscape and track their progress.

## Features

- **Score Distribution**: View problems organized by score
- **Color Rating Analysis**: See the breakdown of problems by AtCoder's color rating system
- **Responsive Design**: Works on desktop and mobile devices
- **Dark/Light Mode**: Toggle between dark and light themes for comfortable viewing
- **Color Themes**: Choose from multiple color themes (green, blue, purple, orange, pink)
- **Interactive Elements**: Hover effects and animations for better user experience

## Technical Details

### Files Structure

- `index.html` - The main HTML file generated from the template
- `template.html` - The template used to generate the final HTML
- `styles.css` - CSS styling for the dashboard
- `script.js` - JavaScript for interactive features
- `assets/` - Contains images and icons

### Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
- **Data Collection**: Python, Selenium
- **Visualization**: Custom CSS animations and styling

## How It Works

1. A Python script using Selenium scrapes AtCoder problem data
2. The data is processed and organized by difficulty and color rating
3. The script generates an HTML file from the template
4. The dashboard displays the data with interactive visualizations

## Usage

Simply open `index.html` in a web browser to view the dashboard. Use the theme toggle button to switch between dark and light modes, and the color theme button to cycle through different color schemes.

## Development

To modify the dashboard:

1. Edit `template.html` for structural changes
2. Modify `styles.css` for styling updates
3. Update `script.js` for new interactive features
4. Run the main Python script to regenerate the dashboard with fresh data

## Credits

Created by [wulukewu](https://github.com/wulukewu)

## License

MIT License