# DevOps Monitoring Project

## Overview
End-to-end DevOps project using Docker, Kubernetes, Prometheus, and Grafana.

## Architecture
App → Kubernetes → Prometheus → Grafana → Alerts

## Features
- Dockerized application
- Kubernetes deployment
- Monitoring with Prometheus
- Grafana dashboards
- CPU & Pod alerts

## Screenshots
(Add screenshots here)

## How to Run
kubectl apply -f k8s/
docker build -t app .
