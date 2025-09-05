
# X-GUARD

**X-GUARD** is a lightweight API scanner built with **FastAPI**. It allows users to scan API endpoints for basic vulnerabilities such as **XSS** and **SQL Injection**. The application features a clean web interface and supports optional token-based authentication.

## Features

* Scan API endpoints for potential **XSS** vulnerabilities.
* Scan API endpoints for potential **SQL Injection** vulnerabilities.
* Supports **token-based authentication** headers.
* Simple and clean web interface using **Jinja2 templates**.
* Fully asynchronous requests using **httpx** for fast scanning.
* No Swagger/Redoc exposed — user-friendly interface only.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/basil171/X-GUARD.git
cd X-GUARD
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the FastAPI application:

```bash
uvicorn main:app --reload
```

2. Open your browser and go to:

```
http://127.0.0.1:8000/
```

3. Enter the API URL, choose the scan type (XSS/SQLi), and provide an optional token if required. Click **Scan** to see results.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---


