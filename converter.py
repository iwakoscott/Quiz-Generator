#IMPORTANT!: THIS PROGRAM REQUIRES A .csv file to be present in the same directory!~ Make sure you have the file in place

import csv

print("--------------------------GRADING PROGRAM-----------------------------")
while True:
	try:
		csv_file_name = raw_input("Enter file name (disregard the .csv): ")
		f = open(csv_file_name + ".csv")
		f.next()
		break
	except StandardError:
		print("%s could not be found. Please try another file name." % (csv_file_name))
while True:
	try:
		n = int(raw_input("How many questions?: "))
		break
	except StandardError:
		print("please try again.")
outfile = open('trash2.csv', 'w')

print("----------------------------------------------------------------------")
csv_f = csv.reader(f)
numbering = ['0','0','0']
nullset = []
for number in range(1,n+1):
	numbering.append(str(number))
for row in csv_f:
	nullset.append(row[1])
	if len(nullset) == 1:
		outfile.write('"' + row[1] + '"' + ', ')
	else:
		outfile.write('\n'+ '"' + row[1] + '"' + ',')
		outfile.write(' ')
	for q in range(3,n+3):
		counter = 0
		if row[q] == '0':	
			outfile.write(numbering[q])
			outfile.write(' ')
x = len(nullset)
outfile.close()

print "\n----------------------------Diagnostic-----------------------------------\n"
print "number of enrolled students: %d" % (x)
f.close()
print "\n", "\n+-------+--------+-------+------+------+-----+-----+-----+------+----+---+"
print"COMPLETE!!!!"
