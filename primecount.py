import sympy
l,r=map(str,input().split())
li=[]
for i in range(l,r+1):
  if sympy.isprime(i):
    li.append(i)
print(len(li))
