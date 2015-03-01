#!/usr/bin/env

import sys

def main():
	if len(sys.argv) !=  2:
		sys.exit("Invalid number of arguments")

	file = getFile(sys.argv[1])

	maxValue = 0
	bestSentence = ""

	for sentence in file.read().split("  "):
		currentValue = getValue(sentence)
		if currentValue  > maxValue:
			bestSentence = sentence
			maxValue = currentValue

	print(bestSentence)

	file.close()

def getFile(fileName):
	try:
		result = open(fileName, "r+")
		return result
	except IOError:
		sys.exit("File could not be found")
	
def getValue(sentence):
	sentence = sentence.lower()
	sentence = ''.join([x for x in sentence if ord(x) < 123 and ord(x) > 96])
	result = 0
	for char in sentence:
		result += (ord(char) - 96)
	return result

if __name__ == '__main__':
	main()
