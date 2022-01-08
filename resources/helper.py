# -*- coding: UTF-8 -*-
import os.path as osp


def get_resources_root():
    return osp.dirname(__file__)


def dict_char_to_huoxing_lang():
    ret = dict()
    fo = open(osp.join(get_resources_root(), '简体-火星文词典.txt'), mode='r')
    for line in fo.readlines():
        ca, cb = line.strip().split('\t')
        ret[ca.strip()] = cb.strip()
    fo.close()
    return ret


def dict_char_to_phonetic():
    print(__file__)
    ret = dict()
    fo = open(osp.join(get_resources_root(), '音近字语料库.txt'), mode='r')
    for line in fo.readlines():
        partitions = line.strip().split(' ')
        if len(partitions) > 1:
            ca, cb = partitions
            ret[ca] = cb
    fo.close()
    return ret


def dict_char_to_shape_closed():
    ret = dict()
    fo = open(osp.join(get_resources_root(), '形近字语料库.txt'), mode='r')
    for line in fo.readlines():
        partitions = line.strip().split(' ')
        if len(partitions) > 1:
            ca, cb = partitions
            ret[ca] = cb
    fo.close()
    return ret


def list_junk_charaters():
    ret = list()
    fo = open(osp.join(get_resources_root(), '无意义符号.txt'), mode='r')
    for line in fo.readlines():
        ret.append(line[0])
    fo.close()
    return ret
