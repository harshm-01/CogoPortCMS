from fastapi import FastAPI
from harshCMS.routes.cms import cms

# Here I have created a FastAPI instance
app = FastAPI()

# Then I included the cms (configuration management system) router into the main application
# FastAPI will route requests to /cms endpoints to the cms router's defined paths
app.include_router(cms)

