#pythoon的内置函数

#filter（） 函数，filter函数可以对某个序列做过滤处理，判断自定义函数的返回结果是否为真来国女，并一次返回处理结果

def fun(x):
    if x >0:
        return x
    else:
        return 0
#range吧生成的列表传给filter，filter依次吧值传入fun，fun最后把结果传给filter，最后将结果yield（yield类似return，不同点是返回值后，程序会继续运行后面的代码）给iterable
#filter 中的过滤函数不能为空
print(filter(fun,range(-5,9)))
list1=list(filter(fun,range(-5,9))) #输出结果
for i in list1:
    print (i,end=" ")

print("\n")
#reduce()  对序列中的连续操作可以通过循环来处理，reduce也可以
def sum(x,y):
    return x+y

from functools import reduce
print(reduce(sum,range(0,10)))#0+1+2+3+...+9



def  power(x):
    return x**x
print(map(power,range(1,5)))
print(list(map(power,range(1,5))))


'''
def even(num):
    if num%2==0:
        return True
    return False
lis = [1,2,3,4,5,6,7,8,9]
res = filter(even,lis)
print('filter..',list(res))  #filter只保留，返回为真的数据，过滤list的作用
res2 = map(even,lis)
print('map..',list(res2))  #map是帮你循环调用函数，这个函数返回就保存什么。

filter.. [2, 4, 6, 8]
map.. [False, True, False, True, False, True, False, True, False]

'''
#eval 将字符串变成表达式求值,eval 也可以将字符串变成一个对象
x=1
print(eval('x+2'))
a="['1','2','3']"
print(type(a))
b=eval(a)
print(type(b))