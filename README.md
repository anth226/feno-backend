 # Feno Backend
    
This is a Feno Backend created in FastAPI with PostgreSQL, Alembic for database migrations, and Pytest for testing that allows users to perform various operations related to user authentication and management.

## Prerequisites

-   Python 3.9 or higher
-   Pipenv package manager
-   PostgreSQL server
    
    
## Project Structure
    
    -   `alembic`: Contains files related to database migration using Alembic.
    -   `app`: Contains the main code for the FastAPI application.
        -   `auth`: Contains code for user authentication using JWT.
        -   `config`: Contains configuration files, including the database configuration.
        -   `models`: Contains the SQLAlchemy database models.
        -   `schemas`: Contains the Pydantic models for data validation and serialization.
        -   `users`: Contains the code for user management, including the API endpoints.
    -   `main.py`: The main entry point of the application.
    -   `.gitignore`: A file specifying files and directories to be ignored by Git.
    -   `alembic.ini`: This file is used to store configuration settings for the Alembic migration tool.
    -   `Pipfile` and `Pipfile.lock`: Files containing information about the project's dependencies.
    
## Local Setup
    
 To set up this project locally, follow these steps:
    
   1.  Clone the repository:
        `git clone https://github.com/anth226/feno-backend` 
        `cd fastapi-starter-template`
        
    2.  Create and activate a virtual environment:
        `pipenv shell` 
        
    3.  Install the project dependencies:
        `pipenv install` 
        
    4.  Run the project:
        `uvicorn main:app --reload` 

## Usage

Start the application by running:
`$ uvicorn main:app --reload` 

Then, go to [http://localhost:8001](http://localhost:8001/) in your browser to see the app.

## Testing

To run the tests, use the following command:

`$ pipenv run pytest` 

## Documentation

The API documentation is available at [http://localhost:8001/docs](http://localhost:8001/docs) and [http://localhost:8001/redoc](http://localhost:8001/redoc).
    
## Database Migrations
This project uses Alembic for database migrations. To create a new migration, run the following command:

   `alembic revision --autogenerate -m "migration name"` 
   
This will apply the migration script to create the database tables and will create a new migration file in the `alembic/versions` directory. To upgrade the database to the latest migration, run the following command:

   `alembic upgrade head` 
    
## API Endpoints
    
 ### Authentication
    
 #### `POST /login`
    
Authenticates a user and returns a JWT token.
    
Request Body:
    
    `{
        "username": "testuser",
        "password": "testpass"
    }` 
    
Response Body:
    
    `{
        "access_token": "jwt-token"
    }` 
    
### Users
    
#### `GET /users`
    
Returns a list of all users.
    Response Body:

    `[
        {
            "id": 1,
            "username": "testuser",
            "email": "testuser@example.com",
            "is_active": True
        },
        {
            "id": 2,
            "username": "zubair",
            "email": "zubair@gmail.com",
            "is_active": False
        }
    ]` 