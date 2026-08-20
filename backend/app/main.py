from fastapi import FastAPI
from .routes import router as api_router

app = FastAPI(title="YouTube Clipper - Backend")
app.include_router(api_router, prefix="/api")

@app.get("/health")
async def health():
    return {"status": "ok"}
