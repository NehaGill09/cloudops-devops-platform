# Architecture

## Components

1. **Flask API** exposes a root information endpoint, a health endpoint, an information endpoint and Prometheus metrics.
2. **Docker** packages the service into a reproducible image. The image uses a slim Python base and a non-root runtime account.
3. **Docker Compose** runs the API and Prometheus on a shared network for a quick local demonstration.
4. **Kubernetes** runs two API replicas behind a ClusterIP Service. Probes detect unhealthy containers; resource requests/limits and a restricted security context provide baseline guardrails.
5. **GitHub Actions** tests every push and pull request, then builds and publishes an image from pushes to main.

## Request flow

A client reaches the API through the Compose port mapping or Kubernetes Service. Prometheus scrapes `/metrics` at a 15-second interval. Health probes call `/healthz`.

## Design trade-offs

This is deliberately small enough to understand and operate locally. It is not a high-availability production architecture: it has no ingress controller, TLS termination, authentication, persistent storage, managed secrets, or external alerting.
