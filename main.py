from fastapi import FastAPI
from fastmcp import FastMCP

app = FastAPI(title="PRODARDOM AI Bridge")

mcp = FastMCP("PRODARDOM AI Bridge")


@mcp.tool()
def create_content_plan(child_name: str):
    """
    Создаёт идею контента для ребёнка-артиста.
    """
    return {
        "child": child_name,
        "ideas": [
            "Reels с тренировкой",
            "Закулисье записи песни",
            "История артиста"
        ]
    }


@app.get("/")
def home():
    return {
        "status": "PRODARDOM AI Bridge работает",
        "message": "MCP коннектор запущен"
    }


@app.get("/health")
def health():
    return {
        "ok": True
    }
mcp_app = mcp.http_app()

app.mount("/mcp", mcp_app)

