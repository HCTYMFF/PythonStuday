#字典的学习
dict={"a":"1","b":"2","c":"3","d":"4","f":"5"}
print(dict)
print(dict["a"])#输出key对应的value
print("a" in dict)#判断key是否存在用in
print("g" in dict)
print(dict.get("a","不存在此key"))#通过字典的get方法取key对应的value，若key不存在，则返回默认值（"不存在此key"）
print(dict.get("g","不存在此key"))
dict.pop("a")#删除一个元素 用pop方法，同时value也被删除


'''
请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
和list比较，dict有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
而list相反：
    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
dict的key必须是不可变对象
'''

#字典的遍历
#遍历key值
print("遍历key值")
for key in dict:
    print(key+':'+dict[key],end=" ")
print("\n")

for key in dict.keys():
    print(key+':'+dict[key],end=' ')

print("\n")
#遍历value
print("遍历value")
for value in dict.values():
    print(value,end=" ")
print("\n")
#遍历字典项
print("遍历字典项")
for kv in dict.items():
    print(kv,end=" ")

print("\n")
#遍历字典键值
print("遍历字典键值")
for key,value  in dict.items():
    print(key+':'+value,end=" ")
print("\n")
for (key,value) in dict.items():
    print(key+':'+value,end=" ")
print("\n")

#将元组变成 字典
abc=("a","b","c","d","a","a","c","d","f","b","f")
#方法1
abc_dict={}
for x in abc:
    if abc.count(x)>=1:
       abc_dict[x]=abc.count(x)

print(abc_dict)
#方法2
bcd_dict={}
for y in abc:
    result=bcd_dict.get(y,-1)
    if result==-1:
        bcd_dict[y]=1
    else:
        bcd_dict[y]=bcd_dict[y]+1
print(bcd_dict)