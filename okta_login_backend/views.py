import requests
from django.http import HttpResponseRedirect, JsonResponse
from requests.auth import HTTPBasicAuth


def login_callback(request, *args, **kwargs):
    okta_code = request.GET.get('code')

    if okta_code is None:
        return JsonResponse({"error": "The Okta Code is None"})

    client_secret = 'your-okta-client-secret-goes-here'
    client_id = 'your-okta-client-id-goes-here'
    domain_url = 'your-okta-domain-url-goes-here'

    # if you're willing to use it with the netlify frontend.. make sure to update the origin
    # e.g. frontend_redirection_url = "https://okta-login-demo.netlify.app/login/callback"

    frontend_redirection_url = "http://localhost:3000/login/callback"
    okta_auth_endpoint = "https://{}/oauth2/default/v1/token".format(domain_url)

    response = dict(requests.post(
        url=okta_auth_endpoint,
        auth=HTTPBasicAuth(client_id, client_secret),
        headers={
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded',
        },
        data={
            'grant_type': 'authorization_code',
            'redirect_uri': 'http://localhost:8000/login/callback/',
            'code': okta_code
        }
    ).json())

    redirect_endpoint = "{}?token_type={}&expires_in={}&access_token={}&scope={}&id_token={}".format(
        frontend_redirection_url,
        response.get('token_type'),
        response.get('expires_in'),
        response.get('access_token'),
        response.get('scope'),
        response.get('id_token'),
    )

    return HttpResponseRedirect(redirect_endpoint)
