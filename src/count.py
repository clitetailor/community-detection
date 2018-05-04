import yaml


with open('followers_list/vnnlp.yaml', 'r') as input_file:
    data = yaml.load(input_file)
    print(len(data))
    