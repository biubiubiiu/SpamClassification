import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Train a spam classifier')
    parser.add_argument('path', help='text file path')
    parser.add_argument('--output', help='path to output file')
    return parser.parse_args()


if __name__ == '__main__':
    pass
