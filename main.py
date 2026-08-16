from fastapi import FastAPI

app = FastAPI(title="PRODARDOM AI Bridge")


@app.get("/")
def home():
    return {
        "status": "PRODARDOM AI Bridge работает",
        "message": "Коннектор запущен"
    }


@app.get("/health")
def health():
    return {
        "ok": True
    }
