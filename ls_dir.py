import os

def ls_dir(path):
    current_dir = os.getcwd()
    print("Current directory:", current_dir)
    for name in os.listdir(path):
        print(os.path.join(path, name))

if __name__ == '__main__':
    ls_dir('.')
