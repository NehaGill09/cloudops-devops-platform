# Troubleshooting

## Compose API does not start

- Check logs: `docker compose logs api`.
- Confirm port 5000 is not already in use.
- Rebuild after dependency or source changes: `docker compose up --build`.

## Prometheus shows the API as down

- Confirm both services are running: `docker compose ps`.
- Check Prometheus targets at `http://localhost:9090/targets`.
- The target must be `api:5000` from inside the Compose network, not localhost.

## Kubernetes reports ImagePullBackOff

- For local Minikube images, build inside Minikube's Docker daemon or load the image with `minikube image load cloudops-api:1.0.0`.
- Confirm the image tag in the Deployment matches the local image.
- Use `kubectl describe pod <pod-name>` to inspect events.

## Pod is not Ready

- Inspect logs with `kubectl logs deployment/cloudops-api`.
- Check the readiness probe path and port.
- Review resource limits and pod events with `kubectl describe pod <pod-name>`.

## GitHub Actions cannot publish

- Confirm the workflow has Packages: write permission.
- Check the Actions run logs and repository package settings.
- Ensure the workflow is running on the main branch; pull requests intentionally do not publish.
