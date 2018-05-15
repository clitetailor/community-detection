import yaml


def main():
    friends_list = []
    with open('friends_list.yaml', 'r') as input_file:
        friends_list = yaml.load(input_file)

    with open('input.txt', 'w') as output_file:
        for item in friends_list:
            output_file.write(str(item[0]))
            output_file.write(' ')
            output_file.write(str(item[1]))
            output_file.write('\n')


if __name__ == '__main__':
    main()
