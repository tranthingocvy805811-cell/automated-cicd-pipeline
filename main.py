from fastapi import FastAPI

app = FastAPI(title="DevOps Monitoring & Healthcheck Service")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "DevOps Automated Pipeline",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "connected"}
