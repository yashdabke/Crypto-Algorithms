import math

def extended(r1,r2):
 a=r1;
 b=r2;
 s1=1;
 s2=0;
 t1=0;
 t2=1;

while(r2>0):
 q=math.floor(r1/r2);
 r=r1-q*r2;
 r1=r2;
 r2=r;
 s=s1-q*s2;
 s1=s2;
 s2=s;
 t=t1-q*t2;
 t1=t2;
 t2=t;
 gcd=r1;
 return (gcd,s1,t1);
 # extended(5,3)

