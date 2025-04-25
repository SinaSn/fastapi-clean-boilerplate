from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv

load_dotenv()

from api.v1 import auth, profile

app = FastAPI(
    title="FastAPI Boilerplate",
    description="FastAPI boilerplate using Clean Architecture, SQLAlchemy, and Alembic",
    version="1.0",
    contact={
        "name": "Sina Saeedinejad",
        "email": "sinasn1996@gmail.com",
    },
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(profile.router, prefix="/api/v1/profile", tags=["Profile"])


@app.get("/", include_in_schema=False)
async def root():
    return {"message": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
