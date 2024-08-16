# Project Name

This project consists of a frontend(ReactJS) and a backend(Django Python) . Follow the steps below to set up and run both parts of the application.

## Backend Setup

1. **Navigate to the backend directory:**

   ```bash
   cd backend
   ```

2. **Install the required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations to set up the database:**

   ```bash
   python manage.py migrate
   ```

4. **Run the backend server:**

   ```bash
   python manage.py runserver
   ```

   The backend server should now be running at `http://127.0.0.1:8000/`.

## Frontend Setup

1. **Navigate to the frontend directory:**

   ```bash
   cd ../fe
   ```

2. **Install the dependencies:**

   ```bash
   yarn install
   ```

3. **Start the frontend server:**

   ```bash
   yarn start
   ```

   The frontend server should now be running at `http://localhost:3000/`.

## Accessing the Application

- **Frontend**: Open `http://localhost:3000/` in your browser.
- **Backend**: The API should be accessible at `http://127.0.0.1:8000/`.

## Handling CORS Issues

If you encounter any CORS (Cross-Origin Resource Sharing) issues while accessing the frontend or backend, you can temporarily disable CORS in your browser for development purposes.

To do this in Google Chrome, follow this guide: [Run Chrome without CORS](https://alfilatov.com/posts/run-chrome-without-cors/).

Please note that this should only be used in a development environment and not in production.

## Additional Notes

- Ensure that the backend is running before starting the frontend, as the frontend may depend on the backend API.
- For development purposes, both servers can be run simultaneously, and any changes made to the code should reflect automatically.

## Troubleshooting

- If you encounter any issues with package installation, ensure your package managers (pip, yarn) are up-to-date.
- Check if the ports `3000` (frontend) and `8000` (backend) are free. If not, close any application using them or modify the port configuration.
