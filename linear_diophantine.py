def extendedea(a, b):
 if b == 0:
 return a, 1, 0
 else:
 d, x, y = extendedea(b, a % b)
 return d, y, x - (a // b) * y

def linear_diophantine(a, b, c):
 gcd, x, y = extendedea(a, b)
 if c % gcd != 0:
 return None
 else:
 x *= c // gcd
 y *= c // gcd
 return x, y

# linear_diophantine( 20,5,100)

