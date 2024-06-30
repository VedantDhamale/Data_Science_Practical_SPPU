#!/usr/bin/env python3

import sys

for lines in sys.stdin:
	line = lines.strip()
	words = line.lower().split()
	for word in words:
		print(word,1)
		

