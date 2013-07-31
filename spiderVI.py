#!/usr/bin/env python

import sys
import pickle
from bing_search_v3 import search, parse_results

def main():
        term = sys.argv[1]
        searchtype = sys.argv[2]
        spider(term, searchtype)

def spider(term, searchtype):
	p = parse_results(search(term, searchtype))
	try:
		l = pickle.load(open(term+".p", "rb"))
		l.append(p)
		pickle.dump(l, open(term+".p", "wb"))

	except IOError:

		print "there was a problem"
		pickle.dump(p, open(term+".p", "wb"))


if __name__  == "__main__":
        main()

