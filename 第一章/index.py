#-*-coding:utf-8-*-
import random
import sys #sys是处理系统环境的函数集合 使用变量需要使用sys.变量来调用

from sys import path #直接从sys模块导入path，可以直接使用path变量
string="this is a test" #string是一个全局变量，一般定义在文件头部
class Student: #类名大写
    '''
       this is a student "class"
    '''
    __name = " "#私有实例变量前必须有两个下划线
    def __init__(self,name):#定义私有方法
        self.__name= name  #self相当于java中的this
    def getName(self):
        return self.__name
    def compare(self,num1,num2):
        if(num1>num2):  #num1和num2均为局部变量，作用范围仅在compare范围内
            print (num1,"大于",num2)
        elif (num2 > num1):
            print(num1,"小于",num2)
        else:
            global string #必须先引用在使用
            print(string)
            print(num1,"等于",num2)


if __name__=='__main__':
    print ("hello")
    student=Student(random.randrange(1,10,2))
    print(student.__doc__)
    print(student.getName())
    student.compare(2,4)
    student.compare(6,4)
    student.compare(8,8)
    print(path)
    print(sys.argv)#argv是存储输入的变量，默认是当前文件路径名
    x=1;y=2;z=3;#若一行中有多条语句则需要使用多个分号将语句隔开，一行一条语句则可以忽略分号
    sql="select"\
         "username from abc"\
         "where id=1"  #字符串的多行表示
    print (sql)
    print (type(True))#type可以进行类别判断
    i=6
    print(i.__doc__)#__doc__是每个Python的对象属性，这个属性描述这个对象的作用

