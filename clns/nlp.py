#!/usr/bin/python
# -*- Coding: utf-8 -*-

import numpy as np
import re
import treetaggerwrapper as ttw
import MeCab

tt = ttw.TreeTagger(TAGLANG="en")
mecab = MeCab.Tagger("-Ochasen")

def get_yen_ja(s):
    try:
        _s = re.sub(",|、|，", "", s)
        res = re.findall(string=_s, pattern='[0-9億万]+円')
        return res
    except:
        return ""

def get_pref(s):
    try:
        res = re.match(string=s, pattern='([^都道府県]*)(東京都|北海道|(?:京都|大阪)府|.{2,3}県)')
        return res.group(2)
    except:
        return np.NaN

def get_en_tags(s):
    _s = tt.tag_text(s)
    _s = [w.split("\t")[:2] for w in _s]
    return _s

def get_en_tags_set(ids, text_set):
    tags_set = list()
    for id, text in zip(ids, text_set):
        tags = get_en_tags(text)
        tags = [[id] + t for t in tags]
        tags_set += tags
    return tags_set

def get_ja_tags(s):
    tags = mecab.parse(s).split("\n")
    tags = [t.split("\t") for t in tags][:-2]
    tags = [w[0::3] for w in tags]
    return tags

def get_ja_tags_set(ids, text_set):
    tags_set = list()
    for id, text in zip(ids, text_set):
        tags = get_ja_tags(text)
        tags = [[id] + t for t in tags]
        tags_set += tags
    return tags_set

if __name__ == "__main__":
    pass