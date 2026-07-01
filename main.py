from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, FileSystemLoader

app = FastAPI()

# ایجاد محیط با کش غیرفعال
env = Environment(
    loader=FileSystemLoader("templates"),
    cache_size=0,  # ❌ کش رو خاموش کن
    auto_reload=True
)
templates = Jinja2Templates(env=env)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
