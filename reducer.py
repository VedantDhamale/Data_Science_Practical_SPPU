#!/usr/bin/env python3

import sys

word_count={}

for lines in sys.stdin:
	word,count = lines.strip().split()
	word_count[word] = word_count.get(word,0) + int(count)
	
for word,count in word_count.items():
	print(word,count)
	
