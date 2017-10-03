from django.shortcuts import render,redirect
from requests_oauthlib import OAuth2Session
import constants


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
        client_id=constants.google_client_id,
        redirect_uri=constants.url_callback,        
        scope=constants.google_scope)
    authorization_url, state = google.authorization_url(constants.url_login,constants.url_callback)

    # State is used to prevent CSRF, keep this for later.
    return redirect(authorization_url)

def oauth2callback(request):
    google = OAuth2Session(constants.google_client_id)
    token = google.fetch_token(constants.token_url, client_secret=google.client_secret,
                               authorization_response=constants.request.url)
    context = {
        'name': token
    }
    return render(request,'hello/hello.html',context)
