# FastAPI CRUD Project

A REST API built with FastAPI and PostgreSQL. Supports full CRUD operations for Products and Users.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Server | Uvicorn |
| Language | Python 3.14 |

---

## Project Structure

```
Fastapi_project_1/
├── main.py            ← All API routes
├── database.py        ← DB connection, session, get_db dependency
├── models.py          ← SQLAlchemy table definitions
├── schemas.py         ← Pydantic request/response models
├── requirements.txt   ← Dependencies
├── .env               ← Secrets (not committed to git)
└── docs/
    ├── ARCHITECTURE.md  ← Full architecture guide with code explanations
    └── DEVLOG.md        ← Challenges and decisions log
```

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/RajReddyGangasani/fastapi_crud_project1.git
cd fastapi_crud_project1
```

**2. Create and activate virtual environment**
```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create a `.env` file in the project root**
```
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/fastapi_db
```

**5. Create the database**
```bash
createdb fastapi_db
```

**6. Run the server**
```bash
uvicorn main:app --reload
```

Server runs at `http://127.0.0.1:8000`

---

## API Endpoints

### Products

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| POST | `/products/` | Create a product | `name`, `price`, `stock` |
| GET | `/products` | Get all products | — |
| GET | `/products/{id}` | Get one product | — |
| PATCH | `/products/{id}` | Update a product | any of: `name`, `price`, `stock` |
| DELETE | `/products/{id}` | Delete a product | — |

### Users

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| POST | `/users` | Create a user | `username`, `email`, `password` |
| GET | `/users` | Get all users | — |
| GET | `/users/{id}` | Get one user | — |
| DELETE | `/users/{id}` | Delete a user | — |

### Other

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |

---

## Interactive API Docs

FastAPI auto-generates a Swagger UI. Once the server is running, open:

```
http://127.0.0.1:8000/docs
```

You can test every endpoint directly from the browser — no Postman needed.

---

## Notes

- Passwords are hashed with SHA-256 before storing — plain text never hits the database
- Tables are auto-created on server start via `Base.metadata.create_all()`
- `.env` and `myvenv/` are gitignored — never commit secrets or virtual environments

---

## Documentation

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for a full breakdown of how every component works, including code-level explanations and architecture flow diagrams.
