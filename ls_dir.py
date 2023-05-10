import os

def print_directory_contents(path):
    for name in os.listdir(path):
        print(os.path.join(path, name))

if __name__ == '__main__':
    print_directory_contents('.')
