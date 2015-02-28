#!/usr/bin/env

import sys

def main():
	if len(sys.argv) !=  2:
		sys.exit("Invalid number of arguments")
	
	if not isNumber(sys.argv[1]):
		sys.exit("Input is not a valid number")
	
	num = int(sys.argv[1])

	
	print('Original Input: {0}\nHexadecimal: {0:#x}\nBinary: {0:#010b}'.format(num))

def isNumber(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

if __name__ == '__main__':
	main()
