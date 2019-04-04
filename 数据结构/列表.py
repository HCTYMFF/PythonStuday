#列表
#列表创建后可以进行 增减操作
list=["1","2","3","4","5","6","6","7","8","9"]
list.append("a")
print(list)
print("list[2]=",list[2])
list.insert(2,"b")#在list的第三个位置插入字母b
print("insert(2,'b')之后",list)
list.remove("6")#移除一个数字6(从左往右),若6不存在 则报错
print("移除6后，的list=",list)
c=list.pop() #从列表末尾移出一个元素
print(c)

#列表的使用
liebiao=["a","b","c","d","e","f","g","h"]
print(liebiao)
print("liebiao[-2]=",liebiao[-2])
print("liebiao[1:3]=",liebiao[1:3])
print("liebiao[-3:-1]=",liebiao[-3:-1])
#遍历 输出
for i in liebiao:
    print(i,end=" ")

print("\n")
liebiao1=['1','2']
liebiao2=liebiao1+liebiao
print(liebiao2)
xiaoliebiao1=['apple']
xiaoliebiao2=['banaba']
xiaoliebiao2.extend(xiaoliebiao1)
print(xiaoliebiao2)

xiaoliebiao2.append(xiaoliebiao1)
for i in xiaoliebiao2:
    print(i,end=" ")
print("\n")
xiaoliebiao3=['123']
xiaoliebiao3 +=['test']
print(xiaoliebiao3)

#列表的查找 排序 反转(元组没有排序和反转)
lbpx=[2,4,13,22,6,8,14,12,54,23,5,3,11,13,53,88,56]
print(lbpx)
print(lbpx.index(13))#打印value为13的索引，若有多个，则显示第一个出现的索引
if(23 in lbpx): #若23在lbpx中则返回true
    print("True")
else:
    print("false")
lbpx.sort() #从小到大排序
print(lbpx)
lbpx.reverse()#列表反转
print(lbpx)

#列表实现堆栈(先进后出)
duizhan=['1','2','3','4','5']
print("duizhan=",duizhan)
duizhan.append("a")
print("duizhan=",duizhan)
duizhan.pop()
print("duizhan=",duizhan)

#队列  先进先出
duilie=['1','2','3','4','5']
print("duilie",duilie)
duilie.append("b")
print("duilie",duilie)
duilie.pop(0)
print("duilie",duilie)


#序列
'''
序列是具有分片和索引的集合
元素  列表 字符串都是属于序列

'''
xulielist=['1','aaa','ddd','ccc','xxx']
xulietuple=('111','222','333','444','555','666','777','888','999')
xuliestr="abcdedalhiss"
print(xulielist[:3])
print(xulietuple[1:-1])
print(xuliestr[3:6])