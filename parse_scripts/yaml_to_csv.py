#!/usr/bin/env python3
import sys
import yaml
import csv

def main():
	file = open(sys.argv[1], 'r')
	fileName = sys.argv[2]
	yamlFile = yaml.load(file, Loader=yaml.FullLoader)
	fileWr = open(sys.argv[2], 'w')
	wr = csv.writer(fileWr)
	for value in yamlFile.values():
		for point in value:
			coords = list(point.values())
			wr.writerow(coords)

main()