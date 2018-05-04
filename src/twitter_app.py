import twitter

import settings


def create_api():
    app_settings = settings.get_app_settings()
    api = twitter.Api(**app_settings, sleep_on_rate_limit=True)
    return api
