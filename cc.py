#!/usr/bin/env python
import sys
import pickle

def main():
	f = sys.argv[1]
	temp = pickle.load(open(f, "r"))
	print "load success"
	main_data = pickle.load(open("core.p", "r+"))
	print "data_load_success"
	main_data.append(temp)
	print "append success"
	pickle.dump(main_data, open("core.p", "r+"))
	print "done"
if __name__ == "__main__":
	main()
