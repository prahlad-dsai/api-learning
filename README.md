# API Data Explorer

A web app that fetches posts from an external REST API and displays them in
the browser, with pagination and filtering by user.

## Features

- Fetches live data from the JSONPlaceholder API
- Pagination with Previous/Next navigation and "Page X of Y"
- Choose posts per page (5, 10, 20, 50)
- Filter posts by user, with the filter and page size kept across pages

## Tech Stack

- Python, FastAPI
- Jinja2 templates, HTML
- `requests` for calling the external API

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/prahlad-dsai/api-learning.git
   cd REPO-NAME
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the server:

   ```bash
   uvicorn webapp:app --reload
   ```

5. Open http://127.0.0.1:8000 in your browser.

## What I Learned

- Optional query parameters in FastAPI
- Server-side pagination using the API's `X-Total-Count` header
- Keeping filter state across pages through URL parameters

## Planned Improvements

- Post detail pages
- Statistics view
- CSS styling
