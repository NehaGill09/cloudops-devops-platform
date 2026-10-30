# Deployment guide

## Docker Compose

1. Install Docker Engine and the Compose plugin.
2. From the repository root run `docker compose up --build`.
3. Check `http://localhost:5000/healthz` and `http://localhost:9090`.
4. Stop with `docker compose down`.

## Local Minikube

1. Install Minikube and kubectl.
2. Start a cluster: `minikube start`.
3. Point the Docker CLI at Minikube's daemon: `eval "$(minikube docker-env)"` (Linux/macOS).
4. Build: `docker build -f docker/Dockerfile -t cloudops-api:1.0.0 .`.
5. Apply resources: `kubectl apply -f kubernetes/configmap.yaml`, then deployment and service YAML.
6. Wait: `kubectl rollout status deployment/cloudops-api`.
7. Access: `kubectl port-forward service/cloudops-api 5000:80`.

## Useful commands

```bash
kubectl get pods,services
kubectl logs deployment/cloudops-api
kubectl describe deployment cloudops-api
kubectl scale deployment/cloudops-api --replicas=3
kubectl rollout history deployment/cloudops-api
kubectl rollout undo deployment/cloudops-api
```

## GHCR image

After a successful main-branch workflow, check the repository's Packages page for the image. For a cluster to pull a private package, create an imagePullSecret and reference it in the Pod spec. Keep credentials out of Git and use least-privilege tokens. The included workflow does not perform cluster deployment.
