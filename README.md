# docker-flask-locust-promethus
# Service Level Objectives (SLOs) for Flask Application

## Introduction
This document defines the Service Level Objectives (SLOs) for the Flask application. The SLOs track the reliability and performance of the application through key metrics such as request count and request latency.

## Key Metrics

### 1. Request Count (`request_count_total`)
- **Description**: Tracks the total number of requests served by the application.
- **Labels**:
  - `method`: HTTP method (GET, POST, etc.)
  - `endpoint`: Endpoint being accessed (e.g., `/`, `/login`)
  - `status_code`: HTTP status code (200, 400, 500, etc.)

### 2. Request Latency (`request_latency_seconds`)
- **Description**: Measures the time taken to process and respond to each request.
- **Labels**:
  - `method`: HTTP method
  - `endpoint`: Endpoint being accessed

## Service Level Objectives (SLOs)

### 1. **Latency SLO** (95% requests under 200ms)
- **Objective**: 95% of requests should complete within 200 milliseconds.
- **Reasoning**: A latency SLO ensures that the application remains fast and responsive, meeting user expectations for performance.
- **Prometheus Query**:
  
  ```promql
  histogram_quantile(0.95, rate(request_latency_seconds_bucket{endpoint="/"}[7d]))

A docker + flask + locust demo project



![Screen Shot 2020-02-07 at 7 08 49 PM](https://user-images.githubusercontent.com/58792/74074716-65a2f580-49dd-11ea-943d-f91229a690ef.png)


![Screen Shot 2020-02-07 at 7 12 18 PM](https://user-images.githubusercontent.com/58792/74074801-c7635f80-49dd-11ea-9273-a04b587bbc05.png)

