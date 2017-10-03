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
    google = OAuth2Session(
        client_id=constants.google_client_id,
        redirect_uri=constants.url_callback)
    code=request.GET['code']
    print code
    token = google.fetch_token(constants.url_token, client_secret=constants.google_client_secret,
                               code=code)

    google = OAuth2Session(
        client_id=constants.google_client_id,
        token=token)
    user_profile=google.get(constants.url_user_profile).json()

    context = {
        'name': user_profile['name']
    }
    return render(request,'hello/hello.html',context)
