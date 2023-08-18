import math
def gcd(a,b):
 while(b>0):
 q=math.floor(a/b);
 r=a-q*b;
 a=b;
 b=r;
 return a;
gcd(25,65)

