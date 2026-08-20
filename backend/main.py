from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import docker_router

app = FastAPI(title="Project 17: Container Suite API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.include_router(docker_router.router)

@app.get("/")
def read_root():
    return {"message": "Project 17 Container Suite Service is online!"}