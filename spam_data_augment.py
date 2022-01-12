import argparse
import math
import random

import jieba
from tqdm import tqdm

from augment import (CharReplacement, InsertJunkCharacters, Repeat,
                     SimplifiedToTraditional, ToEmoji, ToGlyphSimilar,
                     ToHuoxing, ToPhonetic, ToPinyin, WordReplacement, utils)

jieba.setLogLevel(20)  # let jieba be quiet


def parse_args():
    parser = argparse.ArgumentParser(description='Train a spam classifier')
    parser.add_argument('path', help='text file path')
    parser.add_argument('output', help='path to output file')
    parser.add_argument('--shuffle', type=bool, default=False)
    return parser.parse_args()


def run_pipeline(text, pipelines):
    if not isinstance(pipelines, list):
        pipelines = [pipelines]

    result = text
    for pipeline in pipelines:
        result = pipeline(result)

    return result


def process(line):
    """
    Assume text has N chinese characters and M words

    Strategy:
        a. Apply char replacement for n times, n = 1..sqrt(N)
        b. Apply word replacement for m times, m = 1..sqrt(M)/2
        c. Insert k meaningless chars, k = 1..sqrt(N)/2
        d. Combination of a and c, at most 5 times, generate 3 samples
        e. Combination of b and c, at most 5 times, generate 3 samples
        f. Combination of a, b, c, at most 5 times, generate 3 samples
    """
    n_chinese_characters = len(
        [c for c in line if utils.is_chinese_character(c)])
    n_words = len([w for w in jieba.cut(line)])

    sqrt_N = math.sqrt(n_chinese_characters)
    sqrt_M = math.sqrt(n_words)

    n_char_replacement = max(1, math.floor(sqrt_N))
    n_word_replacement = max(1, math.floor(sqrt_M) // 2)
    n_char_insertion = max(1, math.floor(sqrt_N) // 2)

    replacement_ops = [ToEmoji, ToGlyphSimilar, ToHuoxing,
                       SimplifiedToTraditional, ToPhonetic, ToPinyin]
    insertion_ops = [InsertJunkCharacters]

    char_replacements = [CharReplacement(op()) for op in replacement_ops]
    word_replacements = [WordReplacement(op()) for op in replacement_ops]
    char_insertions = [op() for op in insertion_ops]

    result = set()

    # Strategy a
    for n in range(1, n_char_replacement):
        for op in random.sample(char_replacements, 3):
            pipeline = Repeat(op, repeat_times=n)
            aug = run_pipeline(line, pipeline)
            result.add(aug)

    # Strategy b
    for m in range(1, n_word_replacement):
        for op in random.sample(word_replacements, 2):
            pipeline = Repeat(op, repeat_times=m)
            aug = run_pipeline(line, pipeline)
            result.add(aug)

    # Strategy c
    for k in range(1, n_char_insertion):
        for op in char_insertions:
            pipeline = Repeat(op, repeat_times=k)
            aug = run_pipeline(line, pipeline)
            result.add(aug)

    # Strategy d
    all_ops = char_replacements + char_insertions
    for _ in range(3):
        n_augs = random.randint(1, 5)
        pipelines = random.sample(population=all_ops * n_augs, k=n_augs)
        aug = run_pipeline(line, pipelines)
        result.add(aug)

    # Strategy e
    all_ops = word_replacements + char_insertions
    for _ in range(3):
        n_augs = random.randint(1, 5)
        pipelines = random.sample(population=all_ops * n_augs, k=n_augs)
        aug = run_pipeline(line, pipelines)
        result.add(aug)

    # Strategy f
    all_ops = char_replacements + word_replacements + char_insertions
    for _ in range(3):
        n_augs = random.randint(1, 5)
        pipelines = random.sample(population=all_ops * n_augs, k=n_augs)
        aug = run_pipeline(line, pipelines)
        result.add(aug)

    return result


def main():
    args = parse_args()

    result = list()

    fi = open(args.path, 'r', encoding='UTF-8')
    fo = open(args.output, 'w', encoding='UTF-8')

    idx = 0

    result = list()
    for line in tqdm(fi, desc='Process data'):
        result.append(line)  # original text
        result.extend(process(line))  # augmented text

        idx += 1
        if idx > 4:
            break

        if len(result) > 1000:
            if args.shuffle:
                random.shuffle(result)

            for line in result:  # if not shuffle, write back on the fly
                fo.write(f'{line}\n')

    if args.shuffle:
        random.shuffle(result)
    for line in result:
        fo.write(f'{line}')

    fi.close()
    fo.close()


if __name__ == '__main__':
    main()
