str1=input("Enter a string")
li=list(str1)
li[::2],li[1::2]=li[1::2],li[::2]
str1=''.joi(li)
print(str1)
