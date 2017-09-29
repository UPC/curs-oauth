from django.shortcuts import render,redirect
from requests_oauthlib import OAuth2Session

# GOOGLE
google_client_id="xxx"
google_client_secret="yyy"
google_scope = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]
url_login="https://accounts.google.com/o/oauth2/v2/auth"
url_token="https://accounts.google.com/o/oauth2/v2/auth"

url_callback="http://localhost:8000/oauth2callback"

def index(request):
    context = {
        'name': 'Desconegut'
    }
    return render(request,'hello/hello.html',context)
    # TODO: fer una plantilla amb el boto de login
    # TODO: fer la url de callback que guardi la info a la sessio
    # TODO: recarregar la plantilla

def login(request):
    google = OAuth2Session(
        client_id=google_client_id,
        redirect_uri=url_callback,        
        scope=google_scope)
    authorization_url, state = google.authorization_url(url_login,url_callback)

    # State is used to prevent CSRF, keep this for later.
    return redirect(authorization_url)

def oauth2callback(request):
    google = OAuth2Session(google_client_id)
    token = google.fetch_token(token_url, client_secret=google.client_secret,
                               authorization_response=request.url)
    context = {
        'name': token
    }
    return render(request,'hello/hello.html',context)
