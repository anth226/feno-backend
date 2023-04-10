import uvicorn
from fastapi import FastAPI
from app.config.database import Base
from app.config.database import engine
from app.auth import authrouter
from app.users import userrouter
from app.reviews import reviewrouter
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)


@app.get("/")
def hello():
    return "Hello"


app.include_router(authrouter.router)
app.include_router(userrouter.router)
app.include_router(reviewrouter.router)


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
