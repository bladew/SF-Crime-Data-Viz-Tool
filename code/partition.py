#!/usr/bin/python

import csv

# init variable
origin_file = r"..\data\data.csv"
category_file = {}
category_csv = {}

# main loop
with open(origin_file, 'r') as origin:
	origin_reader = csv.reader(origin)
	next(origin_reader)
	for line in origin_reader:
		# check whether we have created the csv pipe for this category. create the file if haven't
		if line[1] not in category_file:
			category_file[line[1]] = open("..\\data\\" + line[1].lower().replace('/','_').replace(' ', '_')+".csv", 'wb')
			category_csv[line[1]] = csv.writer(category_file[line[1]])
			category_csv[line[1]].writerow(["Dates","X","Y"])
		# only record the date, x and y
		category_csv[line[1]].writerow([line[0], line[7], line[8]])

# close all files
for value in category_file.itervalues():
	value.close()