import os


def get_root_dir():
    root_dir = os.path.dirname(os.path.realpath(__file__))
    while root_dir.endswith('SchweizerMesser') != 1:
        root_dir = os.path.abspath(os.path.dirname(root_dir))
    else:
        return root_dir


if __name__ == '__main__':
    get_root_dir()
