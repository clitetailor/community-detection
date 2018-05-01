import yaml


with open('./vnnlp.yaml', 'r') as input_file:
    data = yaml.load(input_file)

    print(len(data))
