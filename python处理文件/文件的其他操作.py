__author__ = 'Administrator'
'''
文件的删除
文件的删除得需要os模块
os 模块常见的处理函数
access(path,mode)按照mode指定的权限范围搁那
chmod(path,mode),修改文件的访稳权限
open(filename,[mode])默认情况下给用户读写执行的权限
remove(path) 移除文件
rename(old,new) old 源文件或者目录，new代表新文件或者目录
stat(path) 返回path指定文件的属性
fstat（path）返回打开文件的所属属性
startfile(filepath)用关联程序打开文件
tmpfile()创建一个临时文件，文件创建在操作系统的临时目录中
'''


'''
os.path 模块函数

abspath(path) 返回path的绝对路径
dirname(p) 返回目录的路径
exists(path) 判断文件是否存在
getatime(filename)返回文件的最后访问时间
getctime(filename)返回文件的创建时间
getmtime(filame)返回文件的最后修改时间
getsize(filename) 返回文件的大小
isabs(s)测试路径是否是绝对路径
isdir(path)返回path指定的是否是目录
isfile(path)返回path指定的是否是文件
split(p)对路径进行分隔，以列表的形式返回
splitext(p)从路径中分隔路径的拓展名
splitdrive()从路径中分隔驱动器的名称
walk(top,func,arg)遍历目录数，与os。walk功能相同
'''
import os
#f=open("c:\\users\\administrator\\destop\\111.txt","w+")
f=open("C:\\Users\\Administrator\\Desktop\\111.txt","w+")
fpath=f.name
f.close()
print(os.path.splitext(fpath))
print(os.path.splitdrive(fpath))
if os.path.exists(fpath):
    os.remove(fpath)
    print(f,"删除成功")
else:
    print("文件不存在，不需要删除")

'''
文件的复制
file类没有复制的功能，可以通过read write的方式实现复制
shutil 模块是文件目录的管理接口，copyfile（old，new）函数可以实现文件的复制，同理move(old,new)
'''
fff=open("c:\\Users\\Administrator\\Desktop\\123.txt")
context=fff.read()
ggg=open("c:\\Users\\Administrator\\desktop\\456.txt","w+")
ggg.write(context)
fff.close()
ggg.close()

import shutil

fff=open("c:\\users\\administrator\\desktop\\123.txt")
path="c:\\users\\administrator\\desktop\\789.txt"
path2="c:\\users\\administrator\\desktop\\abc.txt"
shutil.copyfile(fff.name,path) #会复制文件
shutil.copyfile(fff.name,"111.txt")  #这会在python文件的本目录下建立111.txt文件
shutil.move(path,path2)
#shutil.move(path,"../")  这样会在当前python的父目录下生成一个789.txt文件，同时将原来的789.txt文件删除

#用关联程序打开文件
os.startfile(path2)