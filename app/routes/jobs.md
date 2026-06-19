# Jobs API Routes

This document provides details about the jobs routing endpoints defined in `jobs.py`. The endpoints are prefixed with `/jobs` and are categorized under the "Jobs" tag in the OpenAPI documentation.

## Endpoints

### 1. List Countries
- **URL**: `/jobs/countries`
- **Method**: `GET`
- **Description**: Lists all available countries for scraping (e.g., Indeed).
- **Response**: Returns a JSON object containing a list of lowercase country names.
  ```json
  {
    "countries": ["us", "ca", "uk", "..."]
  }
  ```

### 2. List Sites
- **URL**: `/jobs/sites`
- **Method**: `GET`
- **Description**: Lists available websites that can be scraped.
- **Response**: Returns a JSON object containing a list of lowercase site names.
  ```json
  {
    "sites": ["indeed", "linkedin", "..."]
  }
  ```

### 3. Search Jobs
- **URL**: `/jobs/search`
- **Method**: `POST`
- **Description**: Get jobs giving full details of a job with the link for it.
- **Request Body**: Accepts a `JobSearchRequest` schema object containing search parameters.
- **Response**: Returns a JSON object with the total count and a list of job details.
  ```json
  {
    "count": 10,
    "jobs": [
      {
        ...
      }
    ]
  }
  ```
- **Error Handling**: 
  - Propagates existing HTTP exceptions.
  - Returns a `500 Internal Server Error` if an unexpected error occurs during scraping.
