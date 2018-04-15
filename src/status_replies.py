import TwitterAPI
import yaml

import settings
import utils


def get_user_tweet_replies(api, screen_name):
    params = {'q': screen_name}

    r = TwitterAPI.TwitterPager(api, 'search/tweets', params)

    items = []
    for item in r.get_iterator():
        if 'in_reply_to_screen_name' in item and item['in_reply_to_screen_name'] == screen_name:
            items.append(item)

    filename = f'reply_tweets/{screen_name}.yaml'
    utils.ensure_dir(filename)

    with open(filename, 'w') as output_file:
        yaml.dump(items, output_file, default_flow_style=False)


def main():
    app_settings = settings.get_app_settings()
    api = TwitterAPI.TwitterAPI(** app_settings)

    get_user_tweet_replies(api, 'dongng')


if __name__ == '__main__':
    main()
