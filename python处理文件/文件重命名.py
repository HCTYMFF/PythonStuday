__author__ = 'Administrator'
'''
文件的重命名可以使用os下的rename函数进行重命名
'''
import os
path="c:\\users\\administrator\\desktop\\text.txt"
li=os.listdir(".")
print(li)
for list in li:
    pos=list.find(".")
    if list[pos+1:]=="txt": #pos+1: 表示从.后面的开始到结束
        newname=list[:pos+1]+"html"  #pos+1 表示 从开始到.
        os.rename(list,newname)

for  list in li:
    li=os.path.splitext(list)
    print(li)
    if li[1]==".html":
        newname=li[0]+".abc"
        os.rename(li[0]+li[1],newname)

#方法3可以使用 glob模块，用于路径的匹配，返回符合给定条件的文件列表
import glob
aaa=glob.glob("*.abc") #查找当前目录下的所有.abc为后缀的文件
print("glob的返回结果",aaa)
bbb=glob.glob("c:\\w*\\s*\\*.ini") #glob参数满足正则表达式的语法
print(bbb)

