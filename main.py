from utils import finder

if __name__ == '__main__':
    try:
        bugs_1 = finder('bug.txt', 'landscape.txt')
        print('There are {} matches'.format(bugs_1))
        bugs_2 = finder('bug.txt', 'landscape2.txt')
        print('There are {} matches'.format(bugs_2))
    except Exception as ex:
        print(ex)
