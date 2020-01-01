#!/usr/bin/python
#This script is to sort the list of files/folders inside a folder.

import sys,os,shutil
def list(filename):
#	os.listdir(filename)
	finallist=os.listdir(filename)
	finalist=finallist.sort()
	for item in finallist:
		print(item)

def getlist(filename):
	if len(sys.argv)>=2:

		if os.path.exists(filename):
			print('Location exists')
			print('Listing contents...')
			print('******************************')
			list(filename)
		else:
			print("Invalid Directory \n Exiting!!!")
			exit(1)
#	else:
#		print("Invalid Number of Arguments \n Exiting!!! ")
#		exit(2)

def main():
#	getlist(sys.argv[1])
	try:
	
		getlist(sys.argv[1])
	except:
		print("Invalid Number of Arguments")
		exit(2)

if __name__=='__main__':
	main()

