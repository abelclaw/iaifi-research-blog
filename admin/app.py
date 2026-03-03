"""FastAPI admin application for IAIFI blog paper management.

Serves the admin web interface and API routes for paper discovery
and paper listing.
"""

import logging
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from admin.routes.discovery import router as discovery_router
from admin.routes.generation import router as generation_router
from admin.routes.papers import router as papers_router
from admin.routes.pipeline import router as pipeline_router
from admin.routes.posts import router as posts_router
from pipeline.config import settings
from pipeline.db import Database

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(title="IAIFI Blog Admin")

# CORS middleware for dev convenience (localhost origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers BEFORE static file mount
# so /api/* routes take precedence
app.include_router(discovery_router)
app.include_router(generation_router)
app.include_router(papers_router)
app.include_router(posts_router)
app.include_router(pipeline_router)

# Mount figures directory for serving extracted images
# MUST come BEFORE the catch-all "/" mount (Pitfall 1)
figures_path = Path(settings.FIGURES_DIR)
figures_path.mkdir(parents=True, exist_ok=True)
app.mount(
    "/figures",
    StaticFiles(directory=str(figures_path)),
    name="figures",
)

# Mount static files AFTER API routes and /figures
app.mount(
    "/",
    StaticFiles(directory="admin/static", html=True),
    name="static",
)


@app.on_event("startup")
async def startup_event():
    """Initialize database on app start (ensure tables exist)."""
    db = Database(db_path=settings.DB_PATH)
    await db.initialize()
    logger.info("Database initialized on startup")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("admin.app:app", host="0.0.0.0", port=8000, reload=True)
