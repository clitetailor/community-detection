import TwitterAPI

import settings
import twitter


def main():
    app_settings = settings.get_app_settings()
    api = TwitterAPI.TwitterAPI(** app_settings)

    search_term = 'dongng'
    query = {'q': search_term}

    twitter.fetch(api, 'search/tweets', search_term, query)


if __name__ == '__main__':
    main()
