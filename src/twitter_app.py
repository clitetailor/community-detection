from TwitterAPI import TwitterAPI
import yaml
import json

if __name__ == "__main__":
    with open("config.sample.yaml", "r+") as read_stream, \
            open("config.yaml", "w") as write_stream:
        try:
            config = yaml.load(read_stream)
            keys = ["consumer_key", "consumer_secret",
                    "access_token_key", "access_token_secret"]

            for key in keys:
                if config[key] != "<{}>".format(key).replace('_', '-'):
                    yaml.dump(config, write_stream, default_flow_style=False)

                    sample_config = {}
                    for key in keys:
                        sample_config[key] = "<{}>".format(
                            key).replace('_', '-')

                    read_stream.seek(0)
                    yaml.dump(sample_config, read_stream,
                              default_flow_style=False)
                    read_stream.truncate()

                    break

        except yaml.YAMLError as error:
            print(error)

    with open("config.yaml", "r") as read_stream, \
        open("output.yaml", "w") as write_stream:
        try:
            config = yaml.load(read_stream)
            api = TwitterAPI(**config)
            data = {
                'screen_name': 'vnnlp'
            }
            result = api.request('statuses/user_timeline', data)
            r = []
            for item in result:
                r.append(item)

            yaml.dump(r, write_stream)
        except yaml.YAMLError as error:
            print(error)
        except error:
            print(error)
