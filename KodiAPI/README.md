# KodiAPI Explorer

KodiAPI Explorer is a simple but well-structured API test project using `pytest`, `requests`, and JSON Schema
validation.  
It covers basic positive and negative test scenarios using a public API (JSONPlaceholder).

## 📌 Project structure

KodiAPI/
├── KodiAPI/ # Main application logic (API helpers, data)
│ └── api_helpers.py
├── schemas/ # JSON Schemas for response validation
│ ├── user_schema.json
│ └── post_schema.json
├── tests/ # All tests
│ ├── test_users.py
│ └── test_posts.py
├── pytest.ini # Pytest config
├── requirements.txt # Project dependencies
└── README.md # Project description

## 🚀 Features

- GET requests for users and posts
- JSON Schema validation (contract testing)
- Well-structured test logic (separate test and API layers)
- Readable and reusable code
- Easily extendable structure for future tests

## 🔧 Tech stack

- Python 3.10+
- Pytest
- Requests
- JSON Schema (via `jsonschema` library)
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) – public test API

## ▶️ How to run tests

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run all tests:

  ```bash
    pytest -v
```

3. Or run specific test file:
    ```bash
    pytest tests/test_users.py -v
   ```

🧪 Sample test scenario:

def test_get_user_by_id():
   response = requests.get("https://jsonplaceholder.typicode.com/users/1")
   assert response.status_code == 200
   data = response.json()
   assert data["id"] == 1
   assert "username" in data

📌 Author

Created by a QA Automation trainee learning Python, Pytest, and API testing from scratch.
This project is part of my preparation for the first job in IT as a Junior QA Automation Engineer.

