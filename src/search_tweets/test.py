import yaml

data = []
with open("syria.yaml", "r") as input_file:
    data = yaml.load(input_file)

count = 0
with open("syria_text_only.yaml", "a") as output_file:
    for item in data:
        yaml.dump([item['text']], output_file, default_flow_style=False)
        count += 1
        print(count)
