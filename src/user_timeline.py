import TwitterAPI
import yaml

import settings
import store
import utils


def main():
    app_settings = settings.get_app_settings()
    api = TwitterAPI.TwitterAPI(** app_settings)

    store_data = store.get_data()

    search_term = 'vnnlp'
    query = {'screen_name': search_term}

    filename = 'user_timeline/{}.yaml'.format(search_term)

    utils.ensure_dir(filename)

    if 'user_timeline' in store_data and 'max_id' in store_data['user_timeline']:
        query['max_id'] = store_data['user_timeline']['max_id'] - 1

    max_id = None
    try:
        with open(filename, 'a') as output_file:
            r = TwitterAPI.TwitterPager(api, 'statuses/user_timeline', query)

            for tweet in r.get_iterator():
                yaml.dump([tweet], output_file, default_flow_style=False)
                if 'id' in tweet:
                    max_id = tweet['id']

    except KeyboardInterrupt:
        pass

    if not 'user_timeline' in store_data:
        store_data['user_timeline'] = {}

    store_data['user_timeline']['max_id'] = max_id
    store.store_data(store_data)


if __name__ == '__main__':
    main()
