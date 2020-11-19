#!/usr/bin/python3
import sys
import re
import os

for line in sys.stdin:

        # Get the file path
        doc_id = 'big.txt'

        # Get an array of all the words inside the document
        words = re.findall(r'\w+', line.strip())

        # Map the words
        for word in words:
                print("%s\t%s:1" % (word.lower(), doc_id))
