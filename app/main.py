import logging
import time
from fastapi import FastAPI, Request
from app.api.routes import router as api_router
from app.core.config import settings

# Structured logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("urban-intelligence-ai-engine")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI-powered engine for urban intelligence and 3D scene reconstruction."
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"Processed {request.method} {request.url.path} in {process_time:.4f}s")
    return response

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "healthy", "timestamp": time.time()}

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)