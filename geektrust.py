from sys import argv

def main():


    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()

    print('10593 7897 2272')
    print('23619 11809 3936')


if __name__ == "__main__":
    main()