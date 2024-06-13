from fastapi import FastAPI
from harshCMS.routes.cms import cms


app = FastAPI()


app.include_router(cms)

