import time
import TwitterAPI
import yaml

import twitter
import utils


def main():
    api = twitter.create_api()
    utils.ensure_dir('followers_list/vnnlp.yaml')

    next_cursor = None

    while next_cursor != 0 and next_cursor != '0':
        try:
            with open('followers_list/vnnlp.yaml', 'a') as output_file:
                data = {'screen_name': 'vnnlp'}

                if next_cursor:
                    data['cursor'] = next_cursor

                r = api.request('followers/list', data)

                for item in r:
                    yaml.dump([item], output_file)

                    print(item['screen_name'])

                    if 'next_cursor' in item:
                        next_cursor = item['next_cursor']

                time.sleep(60)

        except TwitterAPI.TwitterRequestError:
            time.sleep(60)


if __name__ == '__main__':
    main()
