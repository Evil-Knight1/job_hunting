from fastapi import FastAPI
from app.routes.jobs import router as jobs_router

app = FastAPI(
    title="JobSpy API",
    version="1.0.0",
)

app.include_router(jobs_router)


@app.get("/")
def root():
    return {"message": "JobSpy API is running"}