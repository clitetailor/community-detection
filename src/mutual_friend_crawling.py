import time
import tweepy
import yaml

import settings


def main():
    app_settings = settings.get_app_settings()

    auth = tweepy.OAuthHandler(
        app_settings['consumer_key'], app_settings['consumer_secret'])
    auth.set_access_token(app_settings['access_token_key'],
                          app_settings['access_token_secret'])

    api = tweepy.API(auth)
    search_term = 'vnnlp'
    mutual_friend_crawling(api, search_term)


def mutual_friend_crawling(api, search_term):
    info_queue = []
    score_map = {}

    user = api.get_user(search_term)

    info_queue.append(user)
    score_map[user.screen_name] = 0

    visited = []

    try:
        while info_queue:
            score_ref_map = {}
            max_score = 0

            for user in info_queue:
                score_ref_map[user.screen_name] = score_map[user.screen_name] / \
                    user.friends_count + 1

                max_score = max(max_score, score_ref_map[user.screen_name])

            next_nodes = []

            for user in info_queue:
                if score_ref_map[user.screen_name] == max_score:
                    info_queue.remove(user)
                    next_nodes.append(user)

            for user in next_nodes:
                if not user in visited:
                    visited.append(user)
                    print(user.screen_name)

                    for friend in user.friends():
                        if friend in info_queue:
                            score_map[friend.screen_name] += 1
                        else:
                            info_queue.append(friend)
                            score_map[friend.screen_name] = 1

            for user in info_queue:
                score_map[user.screen_name] += 1

            time.sleep(0.5)

    except Exception:
        pass

    with open('mutual_friend_crawling.yaml', 'w') as output_file:
        yaml.dump(visited, output_file, default_flow_style=False)


if __name__ == '__main__':
    main()
