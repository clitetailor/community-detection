import os


def ensure_dir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))


def file_exists(filename):
    return os.path.exists(filename)
