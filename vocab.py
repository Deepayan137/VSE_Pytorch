"""
Constructing and loading dictionaries
"""
import numpy
from collections import OrderedDict, defaultdict
import pdb
def build_dictionary(text):
    """
    Build a dictionary
    text: list of sentences (pre-tokenized)
    """
    wordcount = defaultdict(int)
    for cc in text:
        words = cc.split()
        for w in words:
            wordcount[w] += 1
    
    worddict = defaultdict(int)
    for idx, sidx in enumerate(wordcount.keys()):
        worddict[sidx] = idx + 2   # 0: <eos>, 1: <unk>
    return worddict, wordcount
