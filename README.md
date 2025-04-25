# FastAPI Clean Architecture Boilerplate

This project is a boilerplate for building scalable and maintainable FastAPI applications using the principles of Clean Architecture and the Repository Pattern. It includes tools like Uvicorn for running the application and Alembic for database migrations.

## Features

- **FastAPI**: High-performance web framework for building APIs.
- **Clean Architecture**: Separation of concerns for better maintainability.
- **Repository Pattern**: Abstract data access logic for flexibility and testability.
- **Uvicorn**: ASGI server for running the application.
- **Alembic**: Database migration tool for managing schema changes.

## Project Structure

```
.
├── app
│   ├── api             # API routes
│   ├── application     # Business logic
│   ├── core            # Core configuration
│   ├── domain
│   │   ├── entities    # Database models
│   │   ├── schemas     # Pydantic models for request/response validation
│   ├── infrastructure  # Repository interfaces and implementations
│   ├── utils           # Utilities and extensions
│   └── main.py         # Application entry point
├── alembic             # Alembic migration files
└── .env                # Project environment variables
```

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL (or any other supported database)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SinaSn/fastapi-clean-boilerplate.git
    cd fastapi-clean-boilerplate
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure environment variables in a `.env` file:
    ```
    # Base
    APP_NAME=

    # Security
    SECRET_KEY=
    ACCESS_TOKEN_EXPIRE_MINUTES=
    ALGORITHM=

    # Database
    DB_ENGINE=
    DB_HOST=
    DB_PORT=
    DB_USER=
    DB_PASSWORD=
    DB_NAME=
    ```

### Running the Application

1. Apply database migrations:
    ```bash
    alembic upgrade head
    ```

2. Start the application:
    ```bash
    uvicorn app.main:app --reload
    ```

3. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
