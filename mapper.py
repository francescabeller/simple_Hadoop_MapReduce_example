#!/usr/bin/env python
import sys
import nltk
from nltk.corpus import stopwords

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    stopwords = set(stopwords.words('english'))
    for word in words:
	if word not in stopwords:
            print '%s\t%s' % (word, "1")
