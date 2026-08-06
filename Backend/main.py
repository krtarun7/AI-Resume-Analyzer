from fastapi import FastAPI

from app.api.routes import router as resume_router
from app.api.auth import router as auth_router
from app.database.database import Base, engine

app = FastAPI(
    title="AI Resume Analyzer API",
    description="Backend API",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Register Resume API
app.include_router(resume_router)

# Register Authentication API
app.include_router(auth_router)