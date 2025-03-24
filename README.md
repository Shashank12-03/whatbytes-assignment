# Assignment Project

This repository contains the codebase for the assignment project. Follow the instructions below to set up the environment and configure the database.

## Prerequisites

- [PostgreSQL](https://www.postgresql.org/download/) installed on your system.
- [Node.js](https://nodejs.org/) installed (if applicable).
- A `.env` file for environment variables.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd assignment
```

### 2. Set Up PostgreSQL
1. Start your PostgreSQL server.
2. Create a new database:
    ```sql
    CREATE DATABASE assignment_db;
    ```
3. Create a user and grant privileges:
    ```sql
    CREATE USER assignment_user WITH PASSWORD 'your_password';
    GRANT ALL PRIVILEGES ON DATABASE assignment_db TO assignment_user;
    ```

### 3. Configure the `.env` File
Create a `.env` file in the root directory and add the following variables:
```
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=assignment_db
DATABASE_USER=assignment_user
DATABASE_PASSWORD=your_password
```

### 4. Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### 5. Apply Migrations
Run the following commands to apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

### 7. Test the Application
Open your browser and navigate to `http://127.0.0.1:8000/` to verify the application is running.
```

## Additional Notes
- Ensure your PostgreSQL server is running before starting the application.
- Update the `.env` file as needed for your environment.
