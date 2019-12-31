#!/usr/bin/python3
# This script will take file as commandline argument.
# This script will sort the words from file and print with its count.
import sys
def read_fun(filename):
	f = open(filename,"r")
	temp=f.read().lower().split()
	unelem = set(temp)
	for item in sorted(unelem):
		print(item,temp.count(item))
	f.close()

def main():
	filename=sys.argv[1]
	read_fun(filename)
if __name__=='__main__':
	main()

#.demo.py sample.txt
