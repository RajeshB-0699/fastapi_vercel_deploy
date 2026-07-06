from fastapi import FastAPI
from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi.responses import HTMLResponse
import os

from dotenv import load_dotenv
load_dotenv(override = True)
app = FastAPI()

# @app.get("/")
# def instant():
#     return "Live Production!"

@app.get("/heath")
def health_check():
    return {"status": "healthy"}

@app.get("/", response_class = HTMLResponse)
def instant():
    client = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", api_key = os.environ['GEMINI_API_KEY'])
    message = """
You are on a website that has just been deployed to production for the first time!
Please reply with an enthusiastic announcement to welcome visitors to the site, explaining that it is live on production for the first time!
"""
    result = client.invoke(message)
    reply = result.content.replace("\n", "<br>")
    html = f"<html><head><title>Live in an Instant!</title></head><body><p>{reply}</p></body></html>"
    return html
