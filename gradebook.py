#!/usr/bin/python3
#author:@al_vyn
#written: 25/06/2018

import csv

#Create dictionaries
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
alvyn = {
	"name":"alvyn",
	"homework": [92.0,98.0,92.0,94.0],
	"quizzes": [90.0,80,0,85.0],
	"tests": [95.0,93.0]
}

students = [alvyn,tyler,lloyd,alice]

#Adding functions
def banner(text, ch='=', length=78):
      spaced_text = '%s' % text
      banner = spaced_text.center(length, ch)
      return banner
  
def average(numbers):
	total	=	sum(numbers)
	total	=	float(total)
	result	=	total/len(numbers)
	return result

def get_average(students):
	homework	=	average(students["homework"])
	quizzes		=	average(students["quizzes"])
	tests 		=	average(students["tests"])

	var = 0.1*homework + 0.3*quizzes + 0.6*tests
	return var 

def get_letter_grade(score):
	if score >= 90:
		return "A"
	elif 80 <= score < 90:
		return "B"
	elif 70 <= score < 80:
		return "C"
	elif 60 <= score < 70:
		return "D"
	else:
		return "F"

def get_class_average(students):
	results	=	[]
	for student in students:
		avg = get_average(student)
		results.append(avg)
	return average(results)

#alvyn's average data
alvyn_hw = average(alvyn["homework"])
alvyn_qz = average(alvyn["quizzes"])
alvyn_ts = average(alvyn["tests"])

#alice's average data
alice_hw = average(alice["homework"])
alice_qz = average(alice["quizzes"])
alice_ts = average(alice["tests"])

#tyler's average data
tyler_hw = average(tyler["homework"])
tyler_qz = average(tyler["quizzes"])
tyler_ts = average(tyler["tests"])

#lloyd's average data
lloyd_hw = average(lloyd["homework"])
lloyd_qz = average(lloyd["quizzes"])
lloyd_ts = average(lloyd["tests"])

#write the results to a csv file
print (banner('GradeBook'))
print ("\n")
print ("[+]-->A python script that calculates averages and writes the data to a csv file")

with open('C:\\Users\\User\\Documents\\project\\results.csv', 'w') as csvfile:
	fieldnames = ['S/N', 'NAME', 'HOMEWORK', 'QUIZZES', 'TESTS', 'REMARKS']
	writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

	writer.writeheader()
	writer.writerow({'S/N':1, 'NAME':'Alvyn', 'HOMEWORK': alvyn_hw, 'QUIZZES': alvyn_qz, 'TESTS': alvyn_ts, 'REMARKS':""})
	writer.writerow({'S/N':2, 'NAME':'Alice', 'HOMEWORK': alice_hw, 'QUIZZES': alice_qz, 'TESTS': alice_ts, 'REMARKS':""})
	writer.writerow({'S/N':3, 'NAME':'Lloyd', 'HOMEWORK': lloyd_hw, 'QUIZZES': lloyd_qz, 'TESTS': lloyd_ts, 'REMARKS':""})
	writer.writerow({'S/N':4, 'NAME':'Tyler', 'HOMEWORK': tyler_hw, 'QUIZZES': tyler_qz, 'TESTS': tyler_ts, 'REMARKS':""})

#read and display the results csv file
with open('C:\\Users\\User\\Documents\\project\\results.csv', 'r') as csvfile:
	data = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
	for row in data:
		print (','.join(row))

with open('C:\\Users\\User\\Documents\\project\\results.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print (row['HOMEWORK'], row['QUIZZES'], row['TESTS'], row['REMARKS'])

print ("\n")
print (banner('cha0s'))