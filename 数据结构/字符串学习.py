#字符串和编码学习

#ord()函数取单个字符的整数表示
#chr()函数吧编码转换为对应的字符

print("ord('A')=",ord('A'))
print("ord('中')=",ord('中'))
print("chr(66)=",chr(66))
print("chr(25991)=",chr(25991))
print("\\u4e2d=",'\u4e2d')
print("\'ABC\'.encode('ascii')=",'ABC'.encode('ascii'))
print("b\'ABC\'.decode('ascii')=",b'ABC'.decode('ascii'))
print("\'中文\'.encode('utf-8')=","中文".encode('utf-8'))
print("b\'\\xe4\\xb8\\xad\\xe6\\x96\\x87\'=",b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print("b\'.\\xe4\\xb8\\xad\\xff\'.decode(\'utf-8\', errors=\'ignore\')=",b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
#使用errors=\'igneor\'使得有不存在的字节码也能正常显示，不会报错===

print('\n')
#格式化
print("hello,%s" % 'world')
'''
%运算符就是用来格式化字符串的。
在字符串内部，%s表示用字符串替换，%d表示用整数替换，
有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
如果只有一个%?，括号可以省略

常见的占位符有：
占位符 	替换内容
%d 	整数
%f 	浮点数
%s 	字符串
%x 	十六进制整数
'''''
print('%2d-%02d'%(3,1))
print('%.2f'%(3.1415926))

'''
如果你不太确定应该用什么，%s永远起作用，
它会把任何数据类型转换为字符串：

字符串里面的%是一个普通字符怎么办？
这个时候就需要转义，用%%来表示一个%：
'''


#format()
'''
另一种格式化字符串的方法是使用字符串的format()方法，
它会用传入的参数依次替换字符串内的占位符{0}、{1}……，
不过这种方式写起来比%要麻烦得多：
'''

print("hello,{0}今年{2:.1f}岁了".format("小明",4.25,3.25))
#{2:.1f}表示 格式化第二个出现的浮点数字，小数点后保留1位
print("{:b}".format(250))#格式化为2进制
print("{:o}".format(250))#格式化为8进制
print("{:d}".format(250))#格式化为10进制
print("{:x}".format(250))#格式化为16进制

print('{名字}今天{动作}'.format(名字='陈某某',动作='拍视频'))#通过关键字
grade = {'name' : '陈某某', 'fenshu': '59'}
print('{name}电工考了{fenshu}'.format(**grade))
#通过关键字，可用字典当关键字传入值时，在字典前加**即可


#字符串学习
