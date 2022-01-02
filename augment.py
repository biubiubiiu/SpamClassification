import argparse

from tqdm import tqdm

from augment import pinyin_augment, simplified2traditional_augment


def parse_args():
    parser = argparse.ArgumentParser(description='Train a spam classifier')
    parser.add_argument('path', help='text file path')
    parser.add_argument('--output', help='path to output file')
    return parser.parse_args()


def augment(line):
    augmented = set()
    augmented.update(pinyin_augment(line))
    augmented.update(simplified2traditional_augment(line))
    return augmented


def main():
    args = parse_args()

    output = open(args.output, 'w')
    with open(args.path, 'r', encoding='UTF-8') as f:
        for line in tqdm(f, desc='Process data'):
            for aug in augment(line):
                output.write(aug)
    output.close()


if __name__ == '__main__':
    main()
