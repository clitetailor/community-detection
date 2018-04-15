import TwitterAPI
import yaml

import utils


def fetch(api, resource, search_term, query):
    filename = '{0}/{1}.yaml'.format(resource.replace('/', '_'), search_term)

    utils.ensure_dir(filename)

    tweets = []
    try:
        r = TwitterAPI.TwitterPager(api, resource, query)
        for tweet in r.get_iterator():
            tweets.append(tweet)

    except KeyboardInterrupt:
        pass

    with open(filename, 'w') as output_file:
        yaml.dump(tweets, output_file, default_flow_style=False)


def fetch_one(api, resource, search_term, query):
    filename = '{0}/{1}.yaml'.format(resource.replace('/', '_'), search_term)

    utils.ensure_dir(filename)

    r = api.request(resource, query)
    items = [item for item in r]

    with open(filename, 'w') as output_file:
        yaml.dump(items, output_file, default_flow_style=False)
