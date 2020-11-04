#!/usr/bin/env python3
import csv
import sys

def main():
	x, y, z = [], [], []
	file = open(sys.argv[1], 'r')
	rd = csv.reader(file)
	for row in rd:
		x.append(float(row[0]))
		y.append(float(row[1]))
		z.append(float(row[2]))
		
main()