import yaml

import twitter_app


def main():
    api = twitter_app.create_api()
    followers = api.GetFollowers(screen_name='vnnlp')

    with open('followers_list/vnnlp.yaml', 'w') as output_file:
        yaml.dump([follower.screen_name for follower in followers],
                  output_file, default_flow_style=False)


if __name__ == '__main__':
    main()
