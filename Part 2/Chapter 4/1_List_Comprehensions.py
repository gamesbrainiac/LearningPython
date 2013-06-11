__author__ = 'Nafiul Islam'
__title__ = 'List Comprehensions'


if __name__ == '__main__':
    M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print 'M contains:'
    print M

    col2 = [row[2] for row in M]

