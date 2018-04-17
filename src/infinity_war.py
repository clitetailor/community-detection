import TwitterAPI

import settings
import twitter


def main():
    api = TwitterAPI.TwitterAPI(** settings.get_app_settings())

    twitter.fetch(api, 'search/tweets', 'infinity_war', {'q': '#InfinityWar'})


if __name__ == '__main__':
    main()
