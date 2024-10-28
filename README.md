## Sitterly Application Backend ##
## Overview
This repository contains the backend for the Babysitter Application, built using Python with FastAPI and PostgreSQL. The application allows users to manage babysitter profiles, handle bookings, review sitters, and manage user authentication.

## Features
- **User authentication using JWT**: Secure login and registration for users.
- **PostgreSQL database**: Reliable data storage for user information and profiles.
- **RESTful API endpoints**: Manage profiles, bookings, and reviews through a structured API.
- **Profile management**: Users can create and update sitter profiles, including details like name, city, and hourly rate.
- **Booking system**: Parents can book sitters for specified dates and times.
- **Review system**: Parents can review sitters, and sitters can review parents.


## Technologies Used

- **Programming Language**: Python
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic

## Setup Instructions

### Prerequisites

- Make sure you have Docker installed on your machine.

### 1. Start PostgreSQL

- Run the following command to start a PostgreSQL container:
    ```bash
    docker run --name sitterdb -d -p 5446:5432 -e POSTGRES_PASSWORD=secret postgres
    ```

### 2. Initialize and Activate Your Virtual Environment

- Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Windows use .venv\Scripts\activate
    ```

### 3. Install Dependencies

- Install the required dependencies:
    ```bash
    pip install pipenv
    pipenv install
    ```

### 4. Create Your .env File

- Create a `.env` file in the root directory with the following content:
    ```bash
    DATABASE_URL=postgresql://postgres:secret@localhost:5446/postgres
    JWT_SECRET_KEY=<SECRET_KEY>  # Generate a new secret with `openssl rand -hex 32`
    ```

### 5. Run Database Migrations

- Generate and apply the initial migrations:
    ```bash
    pipenv run alembic revision --autogenerate -m "First revision"
    pipenv run alembic upgrade head
    ```

## Running the Application

- To start the FastAPI application, use:
    ```bash
    pipenv run uvicorn main:app --reload
    ```

- The application will be available at `http://localhost:8000`.



