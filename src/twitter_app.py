import twitter
import yaml
import json

if __name__ == "__main__":
    with open("config.yaml", "r") as read_stream, \
        open("output.yaml", "w") as yaml_file:
        try:
            config = yaml.load(read_stream)
            api = twitter.Api(**config)
            result = api.GetSearch(raw_query="src=typd&q=vnnlp", count=15)
            yaml.dump(result, stream=yaml_file)
        except yaml.YAMLError as error:
            print(error)
