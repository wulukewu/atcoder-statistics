# AtCoder Statistics Tracker

This project fetches problem data from the [AtCoder Problems API](https://kenkoooo.com/atcoder/#/api) and provides a web interface to visualize statistics about AtCoder problems, such as distribution by difficulty and color rating.

## Architecture

The project is now a full-stack application:

-   **Backend:** A Node.js application using Express.js to serve a REST API. It fetches data from the AtCoder Problems API, processes it, and exposes it through various endpoints.
-   **Frontend:** A Vue.js 3 application (built with Vite) that consumes the backend API to display problem statistics in a user-friendly interface.

## Features

-   **Backend API:**
    -   Fetches and processes problem data from AtCoder Problems API.
    -   Provides endpoints for statistics (`/api/stats`), difficulty charts (`/api/chart`), and detailed problem information (`/api/problem_dict`).
-   **Frontend UI:**
    -   Displays contest statistics in tables.
    -   Shows lists of problems with details.
    -   Includes theme (light/dark) and color scheme (normal/difficulty) toggles.
    -   Tabbed interface for different views (planned).

## Setup and Usage

### Backend

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Run the server:**
    ```bash
    node server.js
    ```
    The backend server will start, typically at `http://localhost:3000`.
    You will see a log message like:
    ```
    Server listening at http://localhost:3000
    Fetching data...
    Processing data...
    Data fetched and processed successfully.
    ```

4.  **Available API Endpoints** (base URL: `http://localhost:3000`):
    -   `GET /api/stats`: Retrieves general statistics.
    -   `GET /api/chart`: Retrieves data for difficulty charts.
    -   `GET /api/problem_dict`: Retrieves a dictionary of all problems with their details.
    -   `GET /api/all_data`: Retrieves all the above data in a single response.

### Frontend

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Run the development server:**
    ```bash
    npm run dev
    ```
    The frontend development server will start, typically at `http://localhost:5173` (the exact port might vary if 5173 is in use; check the console output).

4.  Open your browser and navigate to the frontend URL displayed in the console to view the application.

## File Structure

```
atcoder-statistics-tracker/
├── backend/
│   ├── node_modules/      # Backend dependencies (ignored by git)
│   ├── server.js          # Main backend Express server file
│   ├── package.json       # Backend npm package configuration
│   ├── package-lock.json
│   └── .gitignore         # Specifies intentionally untracked files for backend
├── frontend/
│   ├── node_modules/      # Frontend dependencies (ignored by git)
│   ├── public/
│   │   └── favicon.ico
│   ├── src/
│   │   ├── assets/        # Static assets (CSS, images)
│   │   │   └── main.css
│   │   ├── components/    # Vue components (Header, ContestTable, etc.)
│   │   ├── router/        # Vue Router configuration
│   │   │   └── index.js
│   │   ├── views/         # Vue views (HomeView, etc.)
│   │   │   └── HomeView.vue
│   │   ├── App.vue        # Main Vue application component
│   │   └── main.js        # Frontend entry point
│   ├── index.html         # Main HTML file for the frontend
│   ├── package.json       # Frontend npm package configuration
│   ├── package-lock.json
│   ├── vite.config.js     # Vite configuration file
│   └── .gitignore         # Specifies intentionally untracked files for frontend
├── README.md              # This file
└── LICENSE                # Project license (if applicable)
```

## Contributing

We welcome contributions! Here's how you can help:

1.  **Fork the Repository.**
2.  **Create a Branch** (`git checkout -b feature/your-feature-name`).
3.  **Make Changes** and test them locally.
4.  **Commit your changes** with clear commit messages.
5.  **Create a Pull Request (PR)** to the main repository.

## License

This project is licensed under the terms of the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
