def  fun():
    print("成功调用fun()");
class Myclass:
    def myfun(self):
        print("mycalss 中的 myfun");


fun()
myclass=Myclass() #创建类Myclass的实例myclass
myclass.myfun()

if '__name__'=='__main__':
    print("当前为主程序")
else:
    print("当前程序正在被调用")