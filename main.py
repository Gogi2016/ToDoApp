from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
import os

from api.task_routes import task_router
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config

config = Config('.env')

# Set up OAuth for Google login
oauth = OAuth(config)
oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"), 
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

app = FastAPI(
    title="ToDo App API",
    description="Manage tasks for registered users",
    version="1.0.0"
)

app.add_middleware(SessionMiddleware, secret_key="een_zeer_geheime_sleutel")

app.include_router(task_router)

@app.get("/", response_class=FileResponse)
def serve_index():
    return FileResponse(os.path.join(os.path.dirname(__file__), "index.html"))

# Start the Google login process: redirect the user to Google
@app.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for('auth') 
    return await oauth.google.authorize_redirect(request, redirect_uri)

# Handle the callback from Google after login
@app.get("/auth")
async def auth(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)
    response = RedirectResponse(url="/")
    response.set_cookie("user", user["email"])
    return response

app.mount("/", StaticFiles(directory=".", html=True), name="static")