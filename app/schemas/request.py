from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class JobSearchRequest(BaseModel):
    search_term: str

    location: str = ""

    site_names: List[str] = Field(
        default=["linkedin", "indeed", "glassdoor"]
    )

    results_wanted: int = 20
    hours_old: int = 72

    # Filters
    country_indeed: Optional[str] = None

    is_remote: Optional[bool] = None

    job_type: Optional[
        Literal[
            "fulltime",
            "parttime",
            "internship",
            "contract",
        ]
    ] = None