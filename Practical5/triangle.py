#we calculate the triangles by adding each of them.
#the basic way to calculate the dots of each triangle
#dots = 0
#n = int(input())
#dots = n*(n+1)/2
#print(dots)

N = int(input('the number of triangles:'))#N is the number of triangles
dots = 0#the initial value
DOTS = 0#DOTS is the sum of the dots
while N > 0:
    dots = N*(N+1)/2#the dots each triangle have
    DOTS = DOTS + dots#the sum of dots
    N = N-1#to calculate the next dots number of triangle
    if N < 10:
        print(dots)
print(DOTS)
