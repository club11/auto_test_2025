"""task 6"""


def count_file(some_file):
    """
    count_file
    """
    add_str = ''
    with open(some_file, 'r', encoding='utf-8') as file:
        count_str = 0
        count_signs = 0
        count_words = 0
        for line in file:
            count_str += 1
            count_signs += len(line)
            count_words += len(line.split(' '))
        add_str = str(count_str) + ' ' + str(count_signs) + ' ' + str(count_words)
        print(add_str)
    with open(some_file, 'a', encoding='utf-8') as file:
        file.write(add_str)


count_file('test/example.txt')
