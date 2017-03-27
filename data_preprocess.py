__author__ = "Dapeng Li"

import numpy as np

import sys
logs = sys.stderr

from collections import defaultdict

def read_word2vec(f): # returns (num_words, num_dims, d)
    d = {}
    print >> logs, "reading word2vec..."
    for i, line in enumerate(open(f)):
        if i == 0:
            num_words, num_dims = map(int, line.split())
            continue
        line = line.split()
        d[line[0].lower()] = np.array(map(float, line[1:]))
    print >> logs, "read %d words" % i
    return num_words, num_dims, d

if __name__ == "__main__":
    
    num_words, num_dims, dictionary = read_word2vec("word2vec.txt")
    
    train = eval("".join(open("train.json").readlines()))
    f = open("train.txt", "wt")
    for example in train:
        vec = np.zeros(num_dims)
        words = []
        for ingredients in example["ingredients"]:
            for word in ingredients.split():
                try:
                    vec += dictionary[word.lower()]
                except:
                    print >> logs, "warning: %s not in word2vec" % word
                    dictionary[word.lower()] = np.zeros(num_dims) # only warn once
                words.append(word) # N.B.: even if not found, still add word
        vec /= len(words)
        print >> f, example["cuisine"], ",".join(map(str, list(vec))), " ".join(words)
        
    test = eval("".join(open("test.json").readlines()))
    f = open("test.txt", "wt")
    for example in test:
        vec = np.zeros(num_dims)
        words = []
        for ingredients in example["ingredients"]:
            for word in ingredients.split():
                try:
                    vec += dictionary[word.lower()]
                    words.append(word)
                except:
                    print >> logs, "warning: %s not in word2vec" % word
        vec /= len(words)
        print >> f, example["id"], ",".join(map(str, list(vec))), " ".join(words)
        
    
