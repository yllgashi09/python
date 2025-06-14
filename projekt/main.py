from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()
@app.post("/developers/")
def create_developer(developer: Developer):
    return {"message": "Developer created successfully", "developer": developer}

@app.post("/projects/")
def create_projects(project: Project):
    return {"message": "Project created successfully", "Project": Project}