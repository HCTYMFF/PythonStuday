__author__ = 'Administrator'

def arithmrtic(x,y,opertor):
    result={
        "+":x+y,
        "-":x-y,
        "*":x*y,
        "/":x/y
    }
    return result.get(opertor)
print(arithmrtic(1,2,"+"))
#函数可以直接传递一个数据当参数
def fun(*arges):
    print (arges)

fun(1,2,3,4,5,6)

def fun2(*a,**b):#a代表可传入一个数组，**b代表可传入一个字典
    print (a)
    print(b)
fun2(1,2,3,4,5,one="1",two="2")

#若函数中没有一个主体，pass相当于一个占位符，函数返回值为None


#函数的嵌套
def waifun():
    x=1;y=2;m=3;n=4;
    return sum(x,y)*sub(m,n)
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
print(waifun())

#内部函数
def neifun():
    x=1;y=2;n=3;m=4;
    def sum(a,b):
        return a+b
    def sub(n,m):
        return n-m
    return sum(x,y)*sub(m,n)
    #方法2
    #内部函数直接调用外部函数的变量
    # def sum():
    #     return x+y
    # def sub():
    #     return n-m
    # return sum()*sub()
print(neifun())

#函数的阶乘
def digui(n):
    i=1
    if n>1:
        i=n
        n=n*digui(n-1) #递推
    print("%d!="%i,n)
    return n   #回归
digui(5)

#lambda函数
#lambda函数是匿名函数 规则lambda 变量1,变量2:表达式
print((lambda x,y:x+y)(3,2))


def niming():
    m=2;n=4;z=6
    result=lambda m,n,z:m+n*z  #匿名函数不能调用外部函数的变量
    print(result(m,n,z))#手动传参
niming()

#generator 函数定于
# def 函数名（）：
#       yield 表达式

def shengchengqi(n):
    for i in range(n):
        yield  i

r=shengchengqi(4)
print(r.__next__())#python3中使用 __next()__替代next（）
print(next(r))#也可以使用 next(变量)来替代 next（） 两种方法都可以
print(next(r))
print(r.__next__())