# Real-Time AI App Pipeline with ML + CI/CD + Monitoring

✅ ML Spam Classifier  
✅ REST API with FastAPI  
✅ Dockerized Deployment  
✅ CI Pipeline with GitHub Actions  
✅ Monitoring stack coming next!

##  Usage

1 Train model:

python ml/train_model.py

2 Build & run app:

docker build -t ai-app .
docker run -p 8000:8000 ai-app

3 Test API:


curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"text": "Win big prize"}'

 Work in progress ...

- Full monitoring stack: Prometheus + Grafana + Loki

- Docker Compose orchestration

- Deployment to Kubernetes

##  Monitoring Stack

- Prometheus (metrics)
- Grafana (dashboards, http://localhost:3000)
- Loki + Promtail (logs)

### Start Full Pipeline

docker-compose up --build

Access Dashboards:

FastAPI App: http://localhost:8000

Prometheus: http://localhost:9090

Grafana: http://localhost:3000 (user: ***** / pass: *****)


Author
ViorelH — Project 12: Real-Time AI Pipeline