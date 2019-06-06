s1,s2=list(map(str,input().split()))
d1=dict(zip(s1,s2))
d2=dict(zip(s2,s1))
if len(d1)==len(d2):
  print("yes")
else:
  print("no")
