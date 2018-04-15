import os
import yaml


def get_data():
    if os.path.isfile('store.yaml'):
        with open("store.yaml", "r") as store_file:
            data = yaml.load(store_file)

            if data:
                return data

    return {}


def store_data(data):
    with open("store.yaml", "w") as store_file:
        yaml.dump(data, store_file, default_flow_style=False)
