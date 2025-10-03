# AtCoder Statistics

This project fetches difficulty statistics for AtCoder Beginner Contest (ABC) problems from the [AtCoder Problems API](https://kenkoooo.com/atcoder/#/api) and provides a modern web application built with React and Node.js to visualize the distribution of problems by difficulty and color rating.

## Features

- **Modern Stack:** Built with React for the frontend and Node.js/Express for the backend API.
- **API Integration:** Fetches problem statistics from the AtCoder Problems API in real-time.
- **Interactive Visualization:** Color-coded progress circles showing the percentage of problems at each difficulty level for each color rating (Grey, Brown, Green, Cyan, Blue, Yellow, Orange, Red, Bronze, Silver, Gold).
- **Responsive Design:** Fully responsive UI that adapts to different screen sizes.
- **Client-Side Routing:** Uses React Router for seamless navigation between statistics and problem detail pages.
- **Theme Support:** Dark/Light mode toggle and multiple color themes (green, blue, purple, orange, pink).
- **PR Previews:** Automatically generates preview deployments for pull requests.

## Requirements

- Node.js 16+
- npm or yarn

Install the necessary packages:

```bash
npm install
```

## Usage

### Development Mode

1.  Clone the repository:

    ```bash
    git clone git@github.com:wulukewu/atcoder-statistics.git
    cd atcoder-statistics
    ```

2.  Install dependencies:

    ```bash
    npm install
    ```

3.  Start the development server:

    ```bash
    npm run dev
    ```

    This will start the Vite development server at `http://localhost:5173`. The API proxy will forward requests to the backend.

### Production Build

1.  Build the application:

    ```bash
    npm run build
    ```

    This will create an optimized production build in the `dist/` directory.

2.  Start the production server:

    ```bash
    npm run server
    ```

    Or use the combined command:

    ```bash
    npm start
    ```

    The server will run at `http://localhost:3000` and serve both the API and the built React application.

## File Structure

```
atcoder-statistics/
├── server/              # Backend API server
│   └── index.js         # Express server with AtCoder API integration
├── src/                 # React application source
│   ├── components/      # React components
│   │   ├── Dashboard.jsx    # Main statistics dashboard
│   │   ├── StatsTable.jsx   # Statistics table component
│   │   └── ProblemList.jsx  # Problem list detail page
│   ├── utils/           # Utility functions
│   │   ├── api.js       # API client for fetching data
│   │   └── theme.js     # Theme management utilities
│   ├── App.jsx          # Main App component with routing
│   └── main.jsx         # Application entry point
├── web-page/            # Static assets (CSS, images, etc.)
│   ├── styles.css       # Main CSS styles
│   └── assets/          # Images and icons
├── dist/                # Production build output (generated)
├── package.json         # Node.js dependencies and scripts
├── vite.config.js       # Vite build configuration
├── index.html           # HTML entry point
├── dict.py              # Legacy: Python script to fetch data
├── main.py              # Legacy: Python script to generate HTML
└── README.md            # This file
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

## Architecture

### Backend (Node.js/Express)

The backend server (`server/index.js`) provides:
- RESTful API endpoint (`/api/data`) that fetches and processes data from AtCoder Problems API
- Static file serving for the built React application
- Color classification based on difficulty thresholds

### Frontend (React)

The frontend application uses:
- **React**: Component-based UI framework
- **React Router**: Client-side routing for SPA navigation
- **Vite**: Fast build tool and development server
- **CSS**: Existing styles from the original project

### Data Flow

1. React app requests data from `/api/data`
2. Backend fetches data from AtCoder Problems API
3. Backend processes and categorizes problems by difficulty and color
4. Frontend displays interactive statistics and problem lists

## Customization

- **Styling:** Modify the `web-page/styles.css` file to customize the appearance.
- **Color Themes:** The app includes 5 color themes (green, blue, purple, orange, pink) that can be cycled through.
- **Backend API:** Modify `server/index.js` to add new endpoints or change data processing logic.
- **Components:** Edit React components in `src/components/` to customize the UI.

## Troubleshooting

- **API Issues:** If you encounter issues with the API, check if the endpoints are still valid and accessible.
- **Data Processing:** If the data structure from the API changes, you may need to update the data processing logic in `main.py`.

## License

This project is licensed under the terms of the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
