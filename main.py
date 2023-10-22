from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app import thankified
from commons import Config

app = FastAPI()

# Add app api services
app.mount(Config.app_context, thankified, name="thankified")