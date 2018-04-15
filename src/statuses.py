import os
import yaml


def get_statuses():
    filename = 'statuses.yaml'
    if os.path.isfile(filename):
        with open(filename, 'w') as statuses_file:
            statuses = yaml.load(statuses_file)

            if statuses:
                return statuses

    return []
