#! /usr/bin/env python
import sys
import pickle

def main():
        file = sys.argv[1]
        l = pickle.load(open(file))
        view_file(l)

def view_file(file):
        for x in file:
                print
                if len(x) == 4:
                        try:
                                print x[0]
                                print x[1]
                                print x[2]
                                print x[3]
                        except:
                                pass
                else:
                        try:
                                for entries in x:
                                        print
                                        for entry in entries:
                                                print entry
                        except:
                                pass
                print

if __name__ == "__main__":
        main()

