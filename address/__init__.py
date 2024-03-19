from django.conf import settings

default_app_config = "address.apps.AddressConfig"

def get_google_api_key():
    """
    Return the Google API Key configured in Settings.
    """
    return getattr(settings, "GOOGLE_API_KEY", None)
    