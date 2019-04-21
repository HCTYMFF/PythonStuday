print("hello")
import re
f1=open("hello.txt")
count=0
for line in f1.readlines():
    #print(line.count("hello"))
    count=count+line.count("hello")
print("hello出现的次数是：",count)
f1.close()

f1=open("hello.txt","r")
f2=open("hello1.txt","a+")
while (True):
   ss=f1.readline()
   if  ss:
       f2.write(ss.replace("hello","大家好"))
   else:
       break
f2.close()
f2=open("hello1.txt")
context=f2.read()
print(context)
f1.close()