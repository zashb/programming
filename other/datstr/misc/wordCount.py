import os
import re
from collections import Counter
from glob import glob


def getWordCount(dir):
    counter = Counter()
    files = glob(os.path.join(dir, ".txt"))
    for file in files:
        with open(file, mode="r") as f:
            words = re.findall(r"\w+", f.read().lower())
            counter += Counter(words)
    return counter


if __name__ == '__main__':
    print(getWordCount("dir"))
