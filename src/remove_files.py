import os
import re


def filter_error_files(files):
    r = []
    for f in files:
        if re.search('\\.error$', f):
            r.append(f)
    return r


def list_all_files_in_folder(folder_name):
    files = os.listdir(folder_name)
    return [f'{folder_name}/{file_name}' for file_name in files]


def main():
    files = list_all_files_in_folder('followers_list')
    files = filter_error_files(files)
    for f in files:
        os.remove(f)


if __name__ == '__main__':
    main()
