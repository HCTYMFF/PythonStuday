a=input("a=")
a=int(a)
b=input("b=")
b=int(b)
if(a==b):
    print("a等于b")
    print("a+b=",a+b)
else:
    print("a不等于b")
    print("a+b=",a+b)
c=input("num=")#python中的input输入都将转换成字符串类型,但是数字类型也可以进行数值运算
print(type(c))

#if elif else
if(a==b):
    print("今天天气好晴朗 a=b")
elif(a>b):
    print("处处好风光 a>b")
else:
    print("好风光 a<b")

#while
number=input("输入几个数字，用逗号分隔").split(",")
print(number)
x=0
while(x<len(number)):
    print(number[x],end=" ")
    x+=1
else:
    print("运行结束")

#for循环  for 变量 in 集合（集合可以是元祖、列表、字典）
for j in range(1,5):  #从0开始，到4结束，步长为1
    print(j,end=" ")
else:
    print(" for循环完全结束 执行else")
