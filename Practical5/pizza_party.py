n = 0
#the initial number of cut is 0
p = (n**2 + n + 2)/2
#the formula of number of pieces of pizza we get
number_of_students = int(input('number of students:',))#input the number of students
while p < number_of_students:
	n = n + 1#take the next number of cuts to find out whether it suits the conditions
	p = (n**2 + n + 2)/2#calculate the pieces
print('the least number of cuts = ',n)
