a=int(input("Enter a number"))
fact=1
if a==0:
  print(fact)
else:
  for i in range(1,a+1):
    fact=fact*i
  print(fact)
