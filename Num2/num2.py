#!/usr/bin/env

import sys
import zipfile
from os.path import basename

# File ordering is not correct
def main():
	if len(sys.argv) !=  2:
		sys.exit("Invalid number of arguments")

	zipfile = getZipFile(sys.argv[1])

	for file in zipfile.infolist():
		filename = basename(file.filename)
		if filename != "":
			print filename, " ",  formatBytes(file.file_size) 

	zipfile.close()

def getZipFile(fileName):
	try:
		result = zipfile.ZipFile(fileName, "r")
		return result
	except IOError:
		sys.exit("Zip File could not be found")
	except zipfile.BadZipfile:
		sys.exit("Not A Zip File")


def formatBytes(numBytes):
	if numBytes > 100000:
		return '{0:.2g} MB'.format(numBytes/ 100000.00)

	if numBytes > 1000:
		return '{0:.2g} KB'.format(numBytes/ 10000.00)

	return '{0:.2g} bytes'.format(numBytes)


if __name__ == '__main__':
	main()
