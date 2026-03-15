# 🚀 Task Tracker API

A RESTful API for managing tasks, built with Python Flask and SQLite.

## Features

- ✅ Full CRUD operations for tasks
- - 🔐 JWT-based authentication
  - - 🗄️ SQLite database with SQLAlchemy ORM
    - - 📝 Input validation and error handling
      - - 📖 Auto-generated Swagger/OpenAPI documentation
        - - 🧪 Unit tests with pytest
          - - 🐳 Docker support
           
            - ## Tech Stack
           
            - - **Python 3.10+**
              - - **Flask** — Lightweight web framework
                - - **SQLAlchemy** — ORM for database operations
                  - - **Flask-JWT-Extended** — JWT authentication
                    - - **Flask-RESTX** — REST API with Swagger docs
                      - - **SQLite** — Embedded database
                        - - **pytest** — Testing framework
                         
                          - ## API Endpoints
                         
                          - | Method | Endpoint | Description | Auth |
                          - |--------|----------|-------------|------|
                          - | POST | `/api/auth/register` | Register new user | No |
                          - | POST | `/api/auth/login` | Login & get token | No |
                          - | GET | `/api/tasks` | Get all tasks | Yes |
                          - | GET | `/api/tasks/<id>` | Get task by ID | Yes |
                          - | POST | `/api/tasks` | Create new task | Yes |
                          - | PUT | `/api/tasks/<id>` | Update task | Yes |
                          - | DELETE | `/api/tasks/<id>` | Delete task | Yes |
                         
                          - ## Getting Started
                         
                          - ### Prerequisites
                          - - Python 3.10 or higher
                            - - pip
                             
                              - ### Installation
                             
                              - ```bash
                                git clone https://github.com/wqlok/task-tracker-api.git
                                cd task-tracker-api

                                python -m venv venv
                                source venv/bin/activate  # On Windows: venv\Scripts\activate

                                pip install -r requirements.txt
                                ```

                                ### Run the Server

                                ```bash
                                python app.py
                                ```

                                The API will be available at `http://localhost:5000`
                                Swagger docs at `http://localhost:5000/api/docs`

                                ### Run Tests

                                ```bash
                                pytest tests/ -v
                                ```

                                ## Project Structure

                                ```
                                task-tracker-api/
                                ├── app.py
                                ├── config.py
                                ├── requirements.txt
                                ├── models/
                                │   ├── __init__.py
                                │   ├── task.py
                                │   └── user.py
                                ├── routes/
                                │   ├── __init__.py
                                │   ├── auth.py
                                │   └── tasks.py
                                ├── tests/
                                │   ├── __init__.py
                                │   └── test_tasks.py
                                ├── LICENSE
                                └── README.md
                                ```

                                ## License

                                MIT License - see [LICENSE](LICENSE) for details.
