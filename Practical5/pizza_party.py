n = 0
p = (n**2 + n + 2)/2
number_of_students = int(input('number of students:',))
while p < number_of_students:
	n = n + 1
	p = (n**2 + n + 2)/2
print('the least number of cuts = ',n)
