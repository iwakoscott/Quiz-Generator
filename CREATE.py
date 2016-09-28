import csv
import subprocess
import shlex
import os
import shutil
''
# Enter Desktop File Path Here:
address = 'C:\\Users\\iwako_000\\Desktop\\'
# ~+~+~+~+~+~+~~+~+~+~+~+~+~~+~+~+~+~+~+~+~~++~+~~++~~+~+~+~++~~+~++~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~

def GenQuiz(quiz_num, size_ofpq, size_ofnq, folder_name, desktop_folder, student_name, problem_set, class_name):
# IMPORTANT! WHEN ANOTHER USER IS TRYING TO USE THIS PROGRAM ON THEIR COMPUTERS YOU MUST DEFINE THE FOLLOWING:
# 1. Create a '.tex' file called exampleFile. i.e 'exampleFile.tex' (this file should be located in the same directory as this .py file)
# 2. Lastly, you must change the file path where you are saving the respective .pdf files!
# 3. You must also create a folder with a folder name of choice! This is folder will hold all of your students pdf files.
# *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~ 

#DEFINED CONSTANTS: Although I am trying to see if I could include this information in the csv file.
#---------------------------------------------------------------------------------------------------
	quiz_number = quiz_num
	Class_name = class_name
	size_of_prev_quiz = size_ofpq
	size_of_new_quiz = size_ofnq
#---------------------------------------------------------------------------------------------------

# Asks the user for folder name and student name
	folder = folder_name
	name = student_name
	string_input = problem_set
	problems = string_input.split()
	problems = [int(a) for a in problems]
#Question Dictionary!
#-----------------------------------------------------------------------------------------------------------------------------
	def Q(x):
		return {
		1: '\n\item[1.] Find the slope of the line through the points $(-10,1)$ and $(-3, -4)$.',
		2: '\n\item[2.] Give an equation for a line parallel to $y= 15x-2$ through the point $(-1,2)$',
		3: '\n\item[3.] Give an equation for a line perpendicular to $y= 15x-2$ through the point $(0, 1)$',
		4: '\n\item[4.] Find the domain of $f(x) = \\frac{(2x^7-13x+5)}{\sqrt{1-3x}}$',
		5: '\n\item[5.] Using $g(x) = \\frac{\sqrt{x}}{1-x^2}$, find $\\frac{g(x+h)-g(x)}{h}$',
		6: '\n\item[6.] If $g(2) = 5$, $g(3) = 5$, $g(4) = 5$, is $g(x)$ a function?',
		7: '\n\item[7.] Given $p(x) = x^2-4x+1$ and $q(x) = \\frac{\sqrt{x}}{x-2}$, find $(q\circ p)(x)$',
		8: '\n\item[8.] Find the limit (if it exists) $\lim_{x\\to 5}\\frac{x-3}{x^2+9}$',
		9: '\n\item[9.] Find the limit (if it exists) $\lim_{x\\to -3}\\frac{x+3}{x^2-9}$',
		10: '\n\item[10.] Sketch a curve where $\lim_{x\\to 2^+}f(x) = 3$, $\lim_{x\\to 2^-}f(x) = 1$ and $f(3) = 2$',
		11: '\n\item[11.] Find any vertical asymptotes of $g(x) = \\frac{x^2-36}{(x-6)^2}$',
		12: '\n\item[12.] Find any horizontal asymptotes of $g(x) = \\frac{x^2-4}{2x^4+8}$',
		13: '\n\item[13.] Determine where the following function is continuous $$f(x) = \left\{ \\begin{array}{lr} 4x+4 & x< -2 \\\\ x^3 + 4 & x\geq -2 \end{array} \\right.$$',
		14: '\n\item[14.] Use the limit definition of derivative to find $\\frac{d}{dx}\left[\\frac{1}{1-x}\\right]$',
		15: '\n\item[15.] Given $f(x) = 6x^6 + \\frac{1}{x^{1/2}} - \cos(x)$, find $f\'(-1)$',
		16: '\n\item[16.] Given $g(t) = (x^5-3x^2+2x-5)(x^4+20x-6)$ find $g\'(t)$',
		17: '\n\item[17.] Find $\\frac{dy}{dx}$ if $y = \\frac{x^2-2x}{\cos(x)}$',
		18: '\n\item[18.] If $f(x) = x^5-2x^3+10x^2$ then find $f^{(4)}(x)$',
		19: '\n\item[19.] If a ball is thrown off of a cliff on some other planet has a height function of $h(t) = -3t^2 + 9t + 1000$ meters after $t$ seconds, then find its velocity and acceleration after 1 second.',
		20: '\n\item[20.] Find $f\'(x)$ if $f(x) = \sin^3(2x)$',
		21: '\n\item[21.] find $\\frac{dy}{dx}$ given $2y^3-3xy^2=7x^2$',
		22: '\n\item[22.] As a spherical balloon inflates, its radius increases at a rate of 1 centimeter per second. Find the rate that the volume increases when the balloon has a radius of 6 centimeters. (note volume $V = \\frac{4}{3}\pi{r}^3$',
		23: '\n\item[23.] On which intervals is $f(x) = x^3-3x^2$ increasing and decreasing?',
		24: '\n\item[24.] Find the absolute (global) extrema of $g(x) = -2x^2 - 8x + 4$ on $[-3, 0]$.',
		25: '\n\item[25.] Good Luck on your finals.... You have no more questions! :)',
		}.get(x,26)
#-----------------------------------------------------------------------------------------------------------------------------
# Code to write LaTeX Files:
	document_class = '\documentclass[11pt]{article}\n'
	preamble = '\usepackage{graphicx}\n\usepackage{amssymb}\n\usepackage{amsmath}\n\usepackage{enumerate}\n'
	packages = '\\textwidth = 6.5in\n\\textheight = 9 in\n' + '\oddsidemargin = 0.0 in\n\evensidemargin = 0.0 in\n' + '\\topmargin = 0.0 in\n\headheight = 0.0 in\n\headsep = 0.0 in\n\n' + '\parskip = 0.2 in'
	begin_document = '\n\\begin{document}'
	end_document = '\n\end{document}'
	title = '\n\\begin{center}\n{\Large ' + Class_name + ': Quiz \\# %d}\n\end{center}' % (quiz_number)

#For Whom?
	nameline = '\n\\begin{flushright}\n' + 'Name: ' + name + '\n\end{flushright}'

	saveFile = open('exampleFile.tex', 'w')
	saveFile.write(document_class)
	saveFile.write(preamble)
	saveFile.write(packages)
# BEGINNING OF THE DOCUMENT!
	saveFile.write(begin_document)
	saveFile.write(nameline)
	saveFile.write(title)
#Begin Enumerate
	saveFile.write('\n\\begin{enumerate}')
	new_problems = []
	for value in range(size_of_prev_quiz+1, size_of_new_quiz+1):
		new_problems.append(value)

# When older problems are not correct:
	if len(problems) > 0:
		for number in problems:
			saveFile.write(Q(number) + '\n\\vspace*{2.5 in}')
# Appending new Quiz Questions here to the old ones:
		for elements in new_problems:
			saveFile.write(Q(elements) + '\n\\vspace*{2.5in}')
# When previous quiz is perfect
	elif len(problems) == 0:
		for num in new_problems:
			saveFile.write(Q(num) + '\n\\vspace*{2.5 in}')
# End Enumerate
	saveFile.write('\n\end{enumerate}')
# END OF DOCUMENT HERE!
	saveFile.write(end_document)
	saveFile.close()
# Compliles the LaTeX file we created above:
	proc = subprocess.Popen(shlex.split('pdflatex exampleFile.tex'))
	proc.communicate()
# Deletes Unnessary Files from folder
	os.unlink('exampleFile.aux')
	os.unlink('exampleFile.log')
	os.rename('exampleFile.pdf', name + '.pdf')
	shutil.move(name+'.pdf', address + desktop_folder + '\\' + folder ) # Darya must change this!
	print "COMPLETE!" + ' :) '

while True:
	try: 
		csv_folder = str(raw_input("Name of .csv file: "))
		f = open(csv_folder)
		csv_f = csv.reader(f)
		break
	except StandardError:
		print "%s does not exist in the directory. Please retype the csv file" % (csv_folder)

class_name = raw_input("Class name: ")
quiz_num = int(raw_input("Quiz #: "))
sizeofpq = int(raw_input("Size of previous quiz: "))
sizeofnq = int(raw_input("Size of new quiz: "))
while True:
	try:
		desktop_folder = raw_input("Enter the name of the folder on your desktop:  ")
		break
	except StandardError:
		print "%s does not exist. Please try another file." % (desktop_folder)
foldername = raw_input("Enter the name of the folder where you want these files stored: ")
new_path = address + desktop_folder + '\\' + foldername
os.makedirs(new_path)
for row in csv_f:
	GenQuiz(quiz_num,sizeofpq,sizeofnq,foldername, desktop_folder, row[0], row[1], class_name)

f.close()
