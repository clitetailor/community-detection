import time
import tweepy
import yaml

import twitter_app
import utils


def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


def load_screen_names_from_vnnlp():
    screen_names = []
    with open('followers_list/vnnlp.yaml', 'r') as input_file:
        screen_names = yaml.load(input_file)
    return screen_names


def exists_screen_name(screen_name):
    return utils.file_exists(f'friends_list/{screen_name}.yaml')


def get_screen_names(users):
    return[user.screen_name for user in users]


def append_screen_names_to_file(screen_name, screen_names):
    with open(f'friends_list/{screen_name}.yaml', 'a') as output_file:
        yaml.dump(screen_names, output_file, default_flow_style=False)


def write_error_to_file(screen_name, e):
    with open(f'friends_list/{screen_name}.error', 'a') as error_file:
        error_file.write(str(e))
        error_file.write('\n')


def fetch_follower(api, screen_name):
    print(f'- {screen_name}')
    for page in limit_handled(tweepy.Cursor(api.followers, screen_name=screen_name).pages()):
        screen_names = get_screen_names(page)
        append_screen_names_to_file(screen_name, screen_names)


def fetch_followers_if_not_exists(screen_name):
    api = twitter_app.create_api()
    if not exists_screen_name(screen_name):
        fetch_follower(api, screen_name)


def main():
    screen_names = load_screen_names_from_vnnlp()
    for screen_name in screen_names:
        fetch_followers_if_not_exists(screen_name)


if __name__ == '__main__':
    main()
