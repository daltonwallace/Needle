#!/usr/bin/env

import sys

def main():

	if len(sys.argv) !=  2:
		sys.exit("Invalid number of arguments")

	file = getFile(sys.argv[1])

	wordTotals = {}

	for word in file.read().split():
		word = word.replace(" ", "").replace(",","").replace(".","").lower()
		if word not in wordTotals:
			wordTotals[word] = 1
		else:
			wordTotals[word] += 1

	if len(wordTotals) == 0:
		sys.exit("No valid words found in file")

	resultKey = "";
	resultValue = 0;

	for key in wordTotals.keys():
		if wordTotals[key] > resultValue:
			resultKey = key
			resultValue = wordTotals[key]

	print("Most used word: %s \nNumber of Occurences: %s" %(resultKey, resultValue))

	file.close()

def getFile(fileName):
	try:
		result = open(fileName, "r+")
		return result
	except IOError:
		sys.exit("File could not be found")
	
if __name__ == '__main__':
	main()
