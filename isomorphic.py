str1=input("Enter string 1")
str2=input("Enter string 2")
if len(str1)==len(str2):
  for i in range(0,len(str1)):
    for j in range(i+1,len(str1)):
      if str1[i]==str1[j]:
        temp=str1[i+1]
        str[i+1]=str[j]
        str[j]=temp
print(str1)
