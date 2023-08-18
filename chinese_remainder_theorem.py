def inv(a, m) :
 
 m0 = m
 x0 = 0
 x1 = 1
 if (m == 1) :
 return 0
 # Apply extended Euclid Algorithm
 while (a > 1) :
 # q is quotient
 q = a // m
 t = m
 # m is remainder now, process
 # same as euclid's algo
 m = a % m
 a = t
 t = x0
 x0 = x1 - q * x0
 x1 = t
 
 # Make x1 positive
 if (x1 < 0) :
 x1 = x1 + m0
 return x1
def findMinX(num, rem, k) :
 
 # Compute product of all numbers
 prod = 1
 for i in range(0, k) :
 prod = prod * num[i]
 # Initialize result
 result = 0
 # Apply above formula
 for i in range(0,k):
 pp = prod // num[i]
 result = result + rem[i] * inv(pp, num[i]) * pp
 
 
 return result % prod
num = [3, 5, 7]
rem = [2, 3, 2]
k = len(num)
print( "x is " , findMinX(num, rem, k))


