import os
from pprint import pprint
import sys 

chrome_options = [
    "--disable-extensions",
    "--disable-popup-blocking",
    "--profile-directory=Default",
    "--ignore-certificate-errors",
    "--disable-plugins-discovery",
    "user_agent=DN"
]

AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow"


LOGIN = sys.argv[1]
PASSWORD = sys.argv[2]
