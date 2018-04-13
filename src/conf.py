import yaml


def check_conf():
    """
    Check app configuration.
    """
    with open("config.sample.yaml", "r+") as read_stream:
        config = yaml.load(read_stream)
        keys = ["consumer_key", "consumer_secret",
                "access_token_key", "access_token_secret"]

        rewrite_config = False

        for key in keys:
            if config[key] != "<{}>".format(key).replace('_', '-'):
                rewrite_config = True

        if rewrite_config:
            with open("config.yaml", "w+") as write_stream:
                yaml.dump(config, write_stream, default_flow_style=False)

            sample_config = {}
            for sub_key in keys:
                sample_config[sub_key] = "<{}>".format(
                    sub_key).replace('_', '-')

            read_stream.seek(0)
            yaml.dump(sample_config, read_stream,
                      default_flow_style=False)
            read_stream.truncate()
