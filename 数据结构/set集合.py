#set学习

#set和dict类似也是一组key的集合但是不存储value
#创建一个set需要提供一个list作为输入的集合
s=set([1,2,34])
print(s)
b=set([1,1,2,2,3,3,4,5])#set会自动过滤重复的值
print(b)
b.add(8)#通过add可以增加元素到set中，重复元素不会被添加进入
b.add(1)
print(b)
b.remove(1)#remove方法可以删除一个元素
print(b)
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
c=s&b
print(c)
d=s|b
print(d)

e=set((1,2,(1,2)))
print(e)

#set的遍历
for a in s:
    print(a,end=" ")

print("\n")
abc=({"a":"1","b":"2","c":"2","d":"3"}) #将字典装进set集合，只会保留key,value被丢弃
for c in abc:
    print(c,end=" ")