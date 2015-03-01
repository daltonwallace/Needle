#!/usr/bin/env

import sys

def main():
	
	# Ensure valid number of arguments
	if len(sys.argv) !=  2:
		sys.exit("Invalid number of arguments")
	
	#  Ensure input is a number
	if not isNumber(sys.argv[1]):
		sys.exit("Input is not a valid number")
	
	#  Cast input to number
	num = int(sys.argv[1])
	
	#  Utilize the string.format() function to do the heavy lifting
	print('Original Input: {0}\nHexadecimal: {0:#010x}\nBinary: {0:#010b}'.format(num))

def isNumber(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

if __name__ == '__main__':
	main()
