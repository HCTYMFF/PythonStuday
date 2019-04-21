__author__ = 'Administrator'
'''
文件的写入
写入文件的方法有两种，一种是write() 一种是writelines（）
write可以吧字符串写入文件，writelines可以吧列表写入文件
'''
ff=open("C:\\Users\\Administrator\\Desktop\\123.txt","w+")
sss="hello"
list=["我是","你爸爸"]
ff.write(sss)
ff.writelines(list)
ff.close()

