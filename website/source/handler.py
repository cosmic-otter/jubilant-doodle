import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware
# from models import Pages, Database

app = FastAPI()

app.add_middleware(GZipMiddleware)
templates = Jinja2Templates(directory=["views"])

# ROOT
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("index.jinja", {"request": request, "data": data})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
