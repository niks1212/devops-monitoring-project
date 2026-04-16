# DevOps Monitoring & Alerting System

## 🚀 Project Overview

This project demonstrates a real-world DevOps monitoring and alerting system deployed on AWS EC2 using Kubernetes. It provides observability, metrics collection, visualization, and alerting for a containerized application.

The system simulates production-like infrastructure where application health, CPU usage, and pod status are continuously monitored using industry-standard tools.

---

## 🏗️ Architecture

User → NodePort Service → Kubernetes Cluster → Application Pods  
                        ↓  
                 Prometheus (Metrics Collection)  
                        ↓  
                 Grafana (Visualization + Alerting)

---

## ⚙️ Tech Stack

- AWS EC2 (Ubuntu)
- Docker
- Kubernetes (Minikube / kubectl)
- Prometheus
- Grafana
- Linux

---

## 📌 Features

### Application Deployment
- Dockerized application
- Kubernetes deployment
- NodePort service exposure

### Monitoring
- CPU & memory monitoring
- Pod-level metrics
- Cluster observability

### Visualization
- Grafana dashboards
- Real-time metrics view

### Alerting
- CPU usage alert
- Pod failure alert
- Real-time alert state monitoring

---

## 🚨 Alert Rules

- CPU usage threshold alert
- Pod restart/failure alert
- Normal state monitoring

---

## 🧪 Testing

Validated using:

- kubectl get pods
- kubectl get svc
- Grafana dashboards
- Pod deletion simulation
- CPU load testing

---

## ▶️ How to Run

### Clone repo
git clone https://github.com/niks1212/devops-monitoring-project.git

### Deploy app
kubectl apply -f k8s/

### Access app
http://<EC2-IP>:30007

### Access Grafana
http://<EC2-IP>:3000

---

## 📊 Key Learnings

- Kubernetes deployment
- Monitoring with Prometheus
- Grafana dashboards
- Alerting & SRE basics
- Incident simulation

---

## 👨‍💻 Author

Nikhil Gorade  
GitHub: https://github.com/niks1212

---

## 🏁 Conclusion

This project demonstrates a production-like DevOps monitoring system with real-time observability and alerting capabilities.
