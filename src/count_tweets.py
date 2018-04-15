import argparse
import os
import glob
import yaml


def count_tweets(filename):
    items = []

    with open(filename, 'r') as input_file:
        items = yaml.load(input_file)

    print(f'{filename}: {len(items)} tweets')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=str, nargs='+')
    args = parser.parse_args()

    for directory in args.directory:
        if os.path.isdir(directory):
            for filename in glob.glob(f'{directory}/*.yaml'):
                count_tweets(filename)
        else:
            count_tweets(directory)


if __name__ == '__main__':
    main()
