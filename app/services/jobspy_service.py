from fastapi import HTTPException
from jobspy import scrape_jobs


def search_jobs(request):
    kwargs = {
        "site_name": request.site_names,
        "search_term": request.search_term,
        "location": request.location,
        "results_wanted": request.results_wanted,
        "hours_old": request.hours_old,
        "is_remote": request.is_remote,
        "job_type": request.job_type,
    }

    if "indeed" in request.site_names and request.country_indeed:
        kwargs["country_indeed"] = request.country_indeed

    try:
        jobs = scrape_jobs(**kwargs)
    except ValueError as e:
        if "Invalid country string" in str(e):
            raise HTTPException(
                status_code=400,
                detail=str(e)
            )
        raise

    return jobs.fillna("").to_dict(orient="records")