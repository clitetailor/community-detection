import yaml

with open("syria.yaml", "r") as input_file:
    data = yaml.load(input_file)

    for item in data:
        print(item)
