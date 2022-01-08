import argparse

from tqdm import tqdm

from augment import Repeat, CharReplacement, SimplifiedToTraditional


def parse_args():
    parser = argparse.ArgumentParser(description='Train a spam classifier')
    parser.add_argument('path', help='text file path')
    parser.add_argument('--output', help='path to output file')
    return parser.parse_args()


def augment(text, pipelines):
    result = text
    for pipeline in pipelines:
        result = pipeline(result)
    return result


def main():
    args = parse_args()

    # example usage
    pipelines = [
        Repeat(CharReplacement(SimplifiedToTraditional()), repeat_times=5)
    ]

    output = open(args.output, 'w', encoding='UTF-8')
    with open(args.path, 'r', encoding='UTF-8') as f:
        for line in tqdm(f, desc='Process data'):
            aug = augment(line, pipelines)
            output.write(aug)
    output.close()


if __name__ == '__main__':
    main()
