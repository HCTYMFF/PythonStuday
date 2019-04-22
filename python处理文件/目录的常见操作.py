'''
python os模块和s.path 提供了一些针对目录操作的函数
'''
'''
os模块常见的目录处理函数


mkdir(path) 创建path指定的一个目录
makedirs(name)创建多级目录 name 表示为 “path1/path2”
removedirs(path)删除path指定的多级目录
listdir(path)列出path指定目录下的所有文件
getcwd() 返回当前工作的目录
chdir(path) 改变当前目录为path指定的目录
walk()遍历目录树
'''

import os
# os.mkdir("hello")
# os.makedirs("hi/hello")
# os.removedirs("hi/hello")
print(os.walk("."))

'''
目录的遍历
目录遍历的两种方式：递归函数和os.walk()
'''

#递归函数
'''
def visdir(path):
    li=os.listdir(path)
   # print(li)
    for p in li:
        pathname=os.path.join(path,p)
        if not os.path.isfile(pathname):
            visdir(pathname)
        else:
            print(pathname)

   # for p in li:
    #    li
visdir("..\\")
'''
'''
os.walk()遍历目录
'''

def valkbianli(path):
    for root,dirs,files in os.walk(path):
        print(root)
        print(files)
        print(dirs)
        for filepath in files:
            print(os.path.join(root,filepath))
valkbianli("../")