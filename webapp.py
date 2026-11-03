from fastapi import FastAPI, Query
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import requests
app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_posts(limit, start, user_id=None):
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {
        "_start": start,
        "_limit": limit,
    }
    if user_id is not None:
        params["userId"] = user_id
    response = requests.get(url, timeout= 10, params=params)
    response.raise_for_status()
    total = int(response.headers.get("X-Total-Count"))
    return response.json(), total
@app.get("/")
def home(request: Request, page: int = Query(1, ge=1), limit: int = Query(5, ge=5, le=50), user_id: int = Query(0, ge=0, le=10)):
    start = (page - 1) * limit
    posts, total = get_posts(limit, start, user_id if user_id != 0 else None)
    total_pages = (total + limit - 1) // limit
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={"posts": posts, "page": page, "limit": limit, "user_id": user_id, "total_pages": total_pages}
)
