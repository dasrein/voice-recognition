#!/usr/bin/env python3

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import os
from dotenv import load_dotenv

load_dotenv()
oauth_client = BackendApplicationClient(client_id=os.getenv("CLIENT_ID"))
token_url = "https://api2.arduino.cc/iot/v1/clients/token"
oauth = OAuth2Session(client=oauth_client)
token = oauth.fetch_token(
    token_url=token_url,
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    include_client_id=True,
    audience="https://api2.arduino.cc/iot",
)

# print(token.get("access_token"))
