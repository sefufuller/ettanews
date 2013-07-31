#! /usr/bin/env python
import sys
import pickle
import random

def main():
	file = sys.argv[1]
	l = pickle.load(open(file))
	hash_file(l)

def hash_file(file):
	y = random.Random()
	for x in file:
    		if len(x) <= 4: 
        		x.append(y.random())
    		else:
        		for fields in x:
            			fields.append(y.random())
	pickle.dump(file, open(sys.argv[1]+".p", "wb")) 
	
if __name__ == "__main__":
	main()
