from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

app = FastAPI()

mcp = FastMCP("PRODARDOM AI Bridge")

@mcp.tool()
def send_task(task: str) -> str:
    """
    Получает задачи от Claude.
    """
    return f"PRODARDOM AI получил задачу: {task}"


@app.get("/")
def home():
    return {
        "status": "PRODARDOM AI Bridge работает",
        "message": "Коннектор запущен"
    }
