import os
import yaml


def main():
    final_list = []

    files = os.listdir('friends_list')
    for f in files:
        user1 = os.path.splitext(os.path.basename(f))[0]

        users = []
        with open(os.path.join('friends_list', f), 'r') as input_file:
            users = yaml.load(input_file)

        if not isinstance(users, list) or len(users) > 600:
            continue

        for user2 in users:
            if not user1 == user2:
                final_list.append([user1, user2])

    files = os.listdir('followers_list')
    for f in files:
        user1 = os.path.splitext(os.path.basename(f))[0]

        users = []
        with open(os.path.join('followers_list', f), 'r') as input_file:
            users = yaml.load(input_file)

        if not isinstance(users, list):
            continue

        for user2 in users:
            if not user1 == user2:
                final_list.append([user2, user1])

    with open('friends_list.yaml', 'w') as output_file:
        yaml.dump(final_list, output_file)


if __name__ == '__main__':
    main()
