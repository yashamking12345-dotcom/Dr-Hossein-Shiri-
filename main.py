from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# 🔍 دیباگ - این رو اینجا اضافه کن
@app.get("/debug")
def debug():
    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    templates_exists = os.path.exists("templates")
    index_exists = os.path.exists("templates/index.html")
    
    return {
        "current_dir": current_dir,
        "files": files,
        "templates_folder_exists": templates_exists,
        "index_exists": index_exists,
        "templates_content": os.listdir("templates") if templates_exists else None
    }

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
