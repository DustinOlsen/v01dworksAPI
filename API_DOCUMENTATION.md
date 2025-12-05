# API Documentation

Base URL: `http://localhost:8011` (default)

## Endpoints

### 1. Check API Status
Checks if the API is running.

- **URL**: `/`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "message": "Privacy Visitor Tracker API is running"
  }
  ```

### 2. Track a Visit
Records a new visit. Call this endpoint from your frontend application when a page loads.

- **URL**: `/track`
- **Method**: `POST`
- **Headers**:
  - `Content-Type: application/json`
- **Body** (JSON, optional):
  ```json
  {
    "path": "/current-page-path"
  }
  ```
  If no body is provided, the path defaults to `/`.

- **Response**:
  ```json
  {
    "status": "ok",
    "country": "US",      // ISO country code or "Unknown"
    "unique": true,       // true if this is a new unique visitor (based on hashed IP)
    "page": "/current-page-path"
  }
  ```

- **Example (cURL)**:
  ```bash
  curl -X POST http://localhost:8011/track \
       -H "Content-Type: application/json" \
       -d '{"path": "/blog/post-1"}'
  ```

### 3. Get Statistics
Retrieves the aggregated visitor statistics.

- **URL**: `/stats`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "total_visits": 150,
    "unique_visitors": 42,
    "countries": {
      "US": 80,
      "CA": 20,
      "GB": 15,
      "Unknown": 35
    },
    "pages": {
      "/": 50,
      "/blog/post-1": 30,
      "/contact": 10
    }
  }
  ```

- **Example (cURL)**:
  ```bash
  curl http://localhost:8011/stats
  ```

## Interactive Documentation

Since this API is built with FastAPI, you can also access interactive documentation generated automatically:

- **Swagger UI**: [http://localhost:8011/docs](http://localhost:8011/docs) - Test endpoints directly in your browser.
- **ReDoc**: [http://localhost:8011/redoc](http://localhost:8011/redoc) - Alternative documentation view.
