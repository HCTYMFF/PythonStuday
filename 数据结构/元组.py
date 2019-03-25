#元组用括号包含元素，一旦创建不可修改
#元组的定义
tuple=(1,23,3,45,56,34,"abc")
print(tuple)
print("tuple[2]=",tuple[2])
for x in tuple:
    print (x,end=" ")

print("\n")
shuzu=("apple")#定义一个字符串
print(type(shuzu))
shuzu1=("apple",)#定义一个一个元素的元组
print(type(shuzu1))
shuzu3=() #定义一个空元组
print(type(shuzu3))

#元组的访问
yuanzu=("apple","banabn","cnm","dl")
yuanzu1=yuanzu[0: 2]#第一个元素开始到第二个元素，不包括第三个元组
yuanzu2=yuanzu[0:-1]#第一个元素开始到 倒数第二个元素结束
print("yuanzu=",yuanzu)
print("yuanzu[0: 2]=",yuanzu1)
print("yuanzu[0:-2]=",yuanzu2)
print("yaunzu[-1]=",yuanzu[-1])
#元组打包
dabao=("1","2","3","4")
#元组解包可以直接将元组内容解包给各个元素
a,b,c,d=dabao #接受解包的变量数必须严格等于元素元素的个数
print("a=",a,"b=",b,"c=",c,"d=",d)

#二元数组
eryuanzu=(("a","b","c"),("1","2","3"),("one","two","three"))
print(eryuanzu)


#元组的遍历
for i in eryuanzu:
    for j in i:
        print(j,end=" ")
print("\n")
print("遍历方法2")
for i in range(len(eryuanzu)):
    print("eryaunzu[%d]"%i,end=" ")
    print("\n")
    for j in range(len(eryuanzu[i])):
        print(eryuanzu[i][j],end=" ")





