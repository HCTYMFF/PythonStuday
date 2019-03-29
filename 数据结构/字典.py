import sys
#字典的学习
dict={"a":"1","b":"2","c":"4","d":"3","f":"5"}
print(dict)
print(dict["a"])#输出key对应的value
print("a" in dict)#判断key是否存在用in
print("g" in dict)
print(dict.get("a","不存在此key"))#通过字典的get方法取key对应的value，若key不存在，则返回默认值（"不存在此key"）
print(dict.get("g","不存在此key"))
dict.pop("a")#删除一个元素 用pop方法，和列表不同，pop必须指定一个key,若key在，则返回key的value，若不存在，则返回key本身
#用del自带函数也可以删除元素
#del(dict['a'])
#清除字典中的所有内容，用clear函数
#dict.clear()


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
#或者 for key in dict:
#          print("dict[%s]" %key,dict[key])
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
#for (k,v) in dict.items():
#      print("dict[%s]"% k,v)

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


#混合字典
dictk={"a":("1","2","3"),"b":["one","two","three"],"c":{"aaa":"ccc"}}
print("dictk[a][2]=",dictk["a"][2])


#update()方法
#字典的合并
hebing1={"key1":"1","key2":"2","key3":"3"}
hebing2={"key3":"4","key4":"5","key5":"6"}
for k in hebing1:
    hebing2[k]=hebing1[k]
print(hebing2)
#字典和并方法类似的内置函数是 update
#上面的代码可以写成  hebing2.update(hebing1) 这样就把hebing1的值复制到了hebing2里

#setdefault
hebing1.setdefault("a")#设置一个默认key a
hebing1.setdefault("a","None")#设置字典key为a的value为None

#字典的排序、复制

print("\n")
print(dict)
#按照key进行排序
print(sorted(dict.items(),key=lambda d:d[0]))
#按照value进行排序
print(sorted(dict.items(),key=lambda  d:d[1]))

#copy() 函数
#dict2=dict.copy() 将dict的内容复制给dict2 ，并清除原先dict2的内容

#深度拷贝
#dict2=copy.deepcopy(dict) #修改了dict2的值，dict不会变
#浅拷贝
#dict3=copy.copy(dict)   #修改了dict3的值，dict也会变


#sys.modules 是全局字典 每加入一个模块就都会在sys.modules中加入这个key
print (sys.modules.keys())#python自动加载的模块
print (sys.modules.values()) #模块对应的引用