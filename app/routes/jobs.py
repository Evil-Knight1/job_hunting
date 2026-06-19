from fastapi import APIRouter, HTTPException
from app.schemas.request import JobSearchRequest
from app.services.jobspy_service import search_jobs
from jobspy import Country, Site, JobType

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/countries")
def list_countries():
    """List available countries for Indeed."""
    return {"countries": [c.name.lower() for c in Country]}

@router.get("/sites")
def list_sites():
    """List available websites to scrape."""
    return {"sites": [s.name.lower() for s in Site]}


@router.post("/search")
def search(request: JobSearchRequest):
    """Get jobs giving full details of a job with the link for it."""
    try:
        jobs = search_jobs(request)
        return {
            "count": len(jobs),
            "jobs": jobs,
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while scraping: {str(e)}")