import yaml

if __name__ == "__main__":
    with open("output.yaml", "r") as output_file:
        items = yaml.load(output_file)
    
    print(len(items))
