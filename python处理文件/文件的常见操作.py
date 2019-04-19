#1文件的创建

#open(file,mode)  file表示打开的文件名，若不存在则新建一个文件名，mode表示打开文件的模式
#mode  类型有 r 只读、r+ 读写  (文件必须存在)
# w 写入 的方式打开，清楚原有的内容，若文件不存在则创建文件
# w+ 以读写的方式打开文件，若原先有内容则先删除原文
#a 以写入的方式打开文件，在文件末尾追加，若文件不存在则创建文件
#a+ 以读写的方式创建文件，在文件尾部添加，若文件不存在则创建文件
#b 以二进制的模式打开
#U 支持所有换行符  “\r \n  \r\n”

#file类常见的属性和方法
'''
属性：
closed  文件关闭则返回true
encoding  显示文件编码类型
name 显示文件名称
mode 文件打开模式

方法:
flush() 将缓存区内容写入磁盘
close() 关闭文件
read([size]) 从文件中读入size字节的数据，作为字符串返回
readline([size]) 从文件中读取1行，作为字节返回，如果指定size，表示每行每次读取的字节数
readlines（[size]）从文件中的每行存储在列表中返回，如果指定size，表示每次读取的字节数
next() 返回下一行的内容
turncate（[size]） 删除size字节的内容
write(str)  把字符串str的内容写入文件
writelines(sequence_of_string) 把字符串序列写入文件
'''

context='''helloworld'''
f=open("C:\\Users\\fengfei\\Desktop\\123.txt",'w')
f.write(context)
f.close()


'''
文件读取操作
文件读取一般 有3中方法  readline()、readlines()、read()
'''

'''
readline() 每次读取文件的一行，需要使用永真表达式读取文件，当文件读取到文件末尾的时候，
依然使用readline函数读取会报错，所以此时需要使用判断，若已经在问价末尾，则中断循环
'''

ff=open("C:\\Users\\fengfei\\Desktop\\456.txt")
print("文件默认打开模式",ff.mode)
print("文件编码格式:",ff.encoding)
while True:
    line=ff.readline()
    if line:
        print(line)
    else:
        break
ff.close()

'''
多行读取方式 readlines()
一次读取多行文件中的内容，通过for循环读取每行内容
'''
print("lines练习")
ff=open("C:\\Users\\fengfei\\Desktop\\456.txt")
lines=ff.readlines()
for line in lines:
    print(line)
ff.close()


'''

read()  read一次性将文本内容复制给变量
'''
print("read练习")
ff=open("C:\\Users\\fengfei\\Desktop\\456.txt")
context=ff.read()
print(context)
ff.close()


ff=open("C:\\Users\\fengfei\\Desktop\\456.txt")
com=ff.read(5) #读取文件的前5个字节的内容
print(com)
print("文件的指针在：",ff.tell(),"位置")
com=ff.read(5)#继续读取文件5个字节的内容
print("文件的指针在：",ff.tell(),"位置")
ff.close()
