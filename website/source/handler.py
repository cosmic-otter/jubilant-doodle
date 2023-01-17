import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware
import requests
from datetime import datetime
# from models import Pages, Database

app = FastAPI()

app.add_middleware(GZipMiddleware)
templates = Jinja2Templates(directory=["views"])

# ROOT
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    page = 1
    jobs = []
    while True:
        results = requests.get(
            headers={
                "PRIVATE-TOKEN": "token-string-here123"
            },
            url=f"http://repo.dev.hrl.internal/api/v4/projects/2/jobs?page={page}&per_page=100"
        )
        jobs = jobs + results.json()

        if len(results.json()) < 100:
            break
            
        page += 1

    data = []
    for job in jobs:
        if len(job['artifacts']) > 1:
            for artifact in job['artifacts']:
                if "artifact" in artifact['filename']:
                    data.append({
                        "job_id": job['id'],
                        "created_at": datetime.strptime(
                            job['created_at'], 
                            "%Y-%m-%dT%H:%M:%S.%fZ"
                        ).strftime("%B-%d-%Y %H:%M %p"),
                        "actor": job['commit']['author_name'],
                        "file_size": job['artifacts_file']['size'],
                        "file_name": job['artifacts_file']['filename']
                    })

    return templates.TemplateResponse("index.jinja", {"request": request, "data": data})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
