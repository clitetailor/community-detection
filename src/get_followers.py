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

                response = r.json()
                if 'next_cursor' in response:
                    next_cursor = response['next_cursor']

                for item in r:
                    print(item['screen_name'])
                    yaml.dump([item], output_file)

                time.sleep(60)
        except TwitterAPI.TwitterRequestError:
            time.sleep(60)


if __name__ == '__main__':
    main()
