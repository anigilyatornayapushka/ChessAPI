# Chess Engine API

## About the Project
Chess Engine API is a project built on Django. It provides API for a chess engine. This project offers an interface to create, play, and analyze chess games.

## Goals
- **Provide a RESTful API** - Utilizing Django REST Framework to create API that allows interaction with the chess engine through HTTPS requests.
- **Improve Performance** - Using Redis as a cache to store data and reduce response time. Also use such technices as pagination, joins in sql requests, multiprocessing.
- **Background Task Processing** - Utilizing Celery with RabbitMQ for handling background tasks, such as game analysis and move generation.
- **Authentication and Security** - Using JSON Web Tokens for secure user authentication.
- **Containerization** - Using Docker for containerizing the application, simplifying deployment and architecture.
- **Data Reliability** - Using PostgreSQL as the main database for flexibility and reliability when dealing with complex queries.

## Installation
- Clone the repository:
```cmd
git clone https://github.com/anigilyatornayapushka/ChessAPI
```
- Create database table in PostgreSQL
- Create .env in \backend\ directory with next fields:
```.env
SECRET_KEY=your_secret_key
DEBUG=True  # Or False for production version
DB_USER=database_user_name
DB_PASS=database_password
DB_HOST=127.0.0.1 # another host for production
DB_PORT=5432
```
- Install dependencies
```cmd
pip install -r tools\requirements\requirements.txt
```

## Main idea

This project is meant as an educational one for studying a new technology stack, and consolidating the material already studied.
