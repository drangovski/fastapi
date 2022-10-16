from fastapi import FastAPI
from .database import engine
from . import models
from .routers import blog, user, authentication


app = FastAPI(swagger_ui_parameters={"operationsSorter": "method"})


# If it doesn't exist, this will create the table in the database. Basically same as migration.
models.Base.metadata.create_all(engine)


# Include Routers
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)


