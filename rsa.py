import random,math  
  
def is_prime(p,q):
 if q>math.sqrt(p):
  return True
 elif p%q==0:
  return False
 else:
  return is_prime(p,q+1)
 
def gen_prim_num():
 p=random.randint(min_rand_num,max_rand_num)
 if is_prime(p,2):
  return p
 else:
  return gen_prim_num()

def prime_pgcd(x,y):
 if x%y==1:
  return True
 elif x%y==0:
  return False
 else:
  return prime_pgcd(y,x%y)
  
def get_e():
 x=random.randint(max(p,q),phi)
 if prime_pgcd(phi,x):
  return x
 else:
  return get_e()

def eea(a,b):
 x=ly=0
 y=lx=1
 while b!=0:
  q,r=a/b,a%b
  a,b,x,lx,y,ly=b,r,lx-x*q,x,ly-y*q,y
 if ly<0:
  return phi+ly
 else:
  return ly
 
def pow_congru(u,v,w):
 if v==0:
  return 1
 elif v%2==0:
  return pow_congru(u*u,v/2,w)%w
 else:
  return u*pow_congru(u*u,v/2,w)%w

min_rand_num=1
max_rand_num=1000
p=gen_prim_num()
q=gen_prim_num()
n=p*q
phi=(p-1)*(q-1)
e=get_e()
d=eea(phi,e)

print "p=",p," / q=",q
print "n=",n," / phi=",phi
print "e=",e," / d=",d

m=random.randint(ord('a'),ord('z'))
print "plain msg:",m
c=pow_congru(m,e,n)
print "encryption:",c
u=pow_congru(c,d,n)
print "decryption:",u