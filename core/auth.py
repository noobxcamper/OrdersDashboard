from msal import PublicClientApplication
from OrdersDashboard.settings import TENANT_ID, APP_ID, SCOPES

app = PublicClientApplication(
    APP_ID,
    authority="https://login.microsoftonline.com/" + TENANT_ID
)

def check_auth():
    # Get logged in accounts
    accounts = app.get_accounts()

    # If no account is cached
    if len(accounts) == 0:
        # Present login page
        interactive_login()

        # Get accounts again and return
        return app.get_accounts()
    else:
        return None

def interactive_login():
    result = app.acquire_token_interactive(SCOPES)

    if "access_token" in result:
        return result["access_token"]
    else:
        print("Error occurred")
        print(result.get("error"))
        print(result.get("error_description"))

def renew_token():
    # Get logged in accounts
    accounts = check_auth()

    # Get the first signed in account only
    result = app.acquire_token_silent(SCOPES, account=accounts[0])

    if "access_token" in result:
        return result["access_token"]
    else:
        print("Error occurred")
        print(result.get("error"))
        print(result.get("error_description"))