# Indian Bank Branch API

A REST API built using FastAPI and PostgreSQL to retrieve, search, and explore Indian banks and their branches.

## Features

- Retrieve a list of banks with pagination.
- Fetch bank details using a bank ID.
- Retrieve bank branches with pagination.
- Fetch branch details using an IFSC code.
- Search branches by IFSC code, branch name, address, city, district, or state.
- Retrieve all branches associated with a specific bank.
- Check database connectivity.
- Automated testing using pytest.

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Data Validation:** Pydantic
- **Testing:** Pytest, HTTPX

## Approach and Methodology

I approached this assignment by building a RESTful API that provides structured access to Indian bank and branch information.

### 1. Database Design
I used PostgreSQL to store the bank and branch records in two related tables. The `banks` table stores bank IDs and names, while the `branches` table stores branch details, including IFSC codes, addresses, cities, districts, and states. The `bank_id` field establishes the relationship between a bank and its branches.

### 2. API Development
I used FastAPI to implement the REST endpoints and SQLAlchemy to interact with PostgreSQL. I separated database models, request/response schemas, database configuration, and CRUD operations into individual modules to keep the code organized and maintainable.

### 3. Endpoint Implementation
I implemented endpoints to retrieve all banks and branches with pagination, fetch individual banks by ID, retrieve branches by IFSC code, list branches belonging to a specific bank, and search branches using relevant fields such as branch name, address, city, district, and state.

### 4. Validation and Error Handling
I used Pydantic schemas and FastAPI's parameter validation to validate inputs. The API returns appropriate HTTP status codes when records are not found or request parameters are invalid. I also added a database health-check endpoint to verify database connectivity.

### 5. Testing
I used Pytest and HTTPX to test the API endpoints, including successful requests, missing records, search functionality, and pagination validation. The test suite passed all eight tests.

### 6. Deployment
I deployed the FastAPI application on Vercel and hosted the PostgreSQL database on Neon. I configured the database connection through environment variables to keep credentials separate from the application code.

## Project Structure

```text
bank-api/
├── app/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── tests/
│   ├── test_banks.py
│   └── test_branches.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Prerequisites

Ensure the following are installed:

- Python 3.10 or later
- PostgreSQL
- Git

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Anushkarai3A/bank-api
cd bank-api
```


### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv venv
```

Activate the environment:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database named `bank_db`.

Ensure the database contains the required `banks` and `branches` tables populated with the Indian bank dataset.

Create a `.env` file in the project's root directory:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/bank_db
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

**Important:** Never commit your `.env` file or database credentials to GitHub.

### 5. Start the API Server

Run:

```powershell
uvicorn app.main:app --reload
```

The server will start at:

http://127.0.0.1:8000

## API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Use Swagger UI to explore endpoints and execute requests directly from your browser.

## API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/health/db` | Check database connectivity |
| GET | `/banks` | Retrieve a list of banks |
| GET | `/banks/{bank_id}` | Retrieve a bank by ID |
| GET | `/banks/{bank_id}/branches` | Retrieve branches belonging to a bank |
| GET | `/branches` | Retrieve a list of branches |
| GET | `/branches/search?q=Mumbai` | Search branches |
| GET | `/branches/{ifsc}` | Retrieve a branch using its IFSC code |

## Usage Examples

### 1. Check API Status

```http
GET /
```

Example response:

```json
{
  "message": "Bank API is running!"
}
```

### 2. Retrieve Banks

```http
GET /banks?skip=0&limit=10
```

Returns a paginated list of banks.

### 3. Retrieve a Specific Bank

```http
GET /banks/1
```

Returns the details of the bank with the specified ID.

### 4. Retrieve Branches

```http
GET /branches?skip=0&limit=10
```

Returns a paginated list of bank branches.

### 5. Search Branches

```http
GET /branches/search?q=Mumbai
```

Searches branch records by IFSC code, branch name, address, city, district, or state.

### 6. Retrieve a Branch by IFSC

```http
GET /branches/ABCD0123456
```

Replace the example IFSC code with the code of the branch you want to retrieve.

### 7. Retrieve Branches for a Bank

```http
GET /banks/1/branches?skip=0&limit=10
```

Returns branches associated with the specified bank ID.

### 8. Check Database Connectivity

```http
GET /health/db
```

Checks whether the API can connect to PostgreSQL.

## Pagination

The bank and branch listing endpoints support pagination through two query parameters:

- `skip`: Number of records to skip. Default: `0`.
- `limit`: Maximum number of records to return. Default: `100`, maximum: `500`.

Example:

```http
GET /branches?skip=20&limit=10
```

This skips the first 20 records and returns up to 10 records.

## Error Handling

The API returns appropriate HTTP status codes for common scenarios:

- `200 OK`: Request completed successfully.
- `404 Not Found`: Requested bank or branch does not exist.
- `422 Unprocessable Entity`: Request parameters fail validation.

## Running Tests

Run the automated test suite from the project root:

```powershell
python -m pytest -v
```

The test suite covers:

- API health and bank listing.
- Handling nonexistent bank records.
- Branch listing and searching.
- Handling invalid IFSC codes.
- Pagination parameter validation.

**Current test status:** 8 tests passed.

## Database Design

The application uses two PostgreSQL tables:

### `banks`

Stores bank information, including:

- `id`
- `name`

### `branches`

Stores branch information, including:

- `ifsc`
- `bank_id`
- `branch`
- `address`
- `city`
- `district`
- `state`

The `bank_id` field links branches to their corresponding banks.

SQLAlchemy manages database interactions between the application and PostgreSQL.

## Security

- Database credentials are stored in environment variables.
- The `.env` file is excluded from version control.
- The `.env.example` file provides a template for local configuration.

## License

The application code is licensed under the MIT License. See the `LICENSE` file for details.

The Indian bank dataset may be subject to separate licensing terms. Refer to the original dataset repository for its applicable license.
