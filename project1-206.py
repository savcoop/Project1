import os
import filecmp
from dateutil.relativedelta import *
from datetime import date, datetime
import matplotlib.pyplot as plt 
from math import ceil


def getData(file):
	file_data = open(file, 'r')
	full_list = []
	for line in file_data.readlines()[1:]:
		line_data = line.split(',')
		new_dict = {'First': line_data[0], 'Last': line_data[1], 'Email': line_data[2],'Class': line_data[3], 'DOB' : line_data[4]}
		full_list.append(new_dict)
	return full_list


def mySort(data,col):
	sorted_data = sorted(data, key = lambda x: x[col])
	final_name = sorted_data[0]["First"] + " " + sorted_data[0]["Last"]
	return final_name

	
def classSizes(data):
	senior_count = 0
	junior_count = 0
	sophomore_count = 0
	freshman_count = 0 
	for x in data:
		if x["Class"] == "Senior":
			senior_count += 1 
		if x["Class"] == "Junior":
			junior_count += 1
		if x["Class"] == "Sophomore":
			sophomore_count += 1
		elif x["Class"] == "Freshman":
			freshman_count += 1 
	class_count = {"Senior": senior_count, "Junior": junior_count, "Sophomore": sophomore_count, "Freshman": freshman_count}
	grade = list(class_count.keys())
	value = list(class_count.values())
	plt.bar(grade,value, label = "Class Distribution")
	plt.show()

	sorted_class_count = sorted(list(class_count.items()), reverse=True, key=lambda x: x[1])


	return sorted_class_count

	
def findMonth(a):
	birthday_dict = {}
	for x in a: 
		month = x['DOB'].split('/')[0]
		birth_strip = month.strip()
		if birth_strip not in birthday_dict:
			birthday_dict[birth_strip] = 1
		else: 
			birthday_dict[birth_strip] += 1

	sorted_birthdays = sorted(birthday_dict.items(), key = lambda x: x[1], reverse= True)

	return int(sorted_birthdays[0][0])

	

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	outFile = open(str(fileName), "w")
	data = sorted(a, key = lambda x: x[str(col)])
	for y in data: 
		first = y["First"]
		last = y["Last"]
		email = y["Email"]
		outFile.write(first + last + email + '\n')
	outFile.close()

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

#URL for where this solution partially came from in case they expect you to cite it:  
#https://stackoverflow.com/questions/2217488/age-from-birthdate-in-python
	ages = []
	today = date.today()
	for x in a[1:]:
		birth_date = datetime.strptime(x['DOB'].strip(), '%m/%d/%Y')
		age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
		ages.append(age)

	total = 0
	for x in ages:
		total += x
	avg_age = ceil(float(total/len(ages)))
	return round(avg_age)

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()