import fun1
#from 模块 import 函数   ，python的引入可以放在文件的任何位置
__doc__='''我模块fun2'''


'''
每个模块都有一个__name__和__doc__,若当前程序正在被运行__name__的值为__main__

__doc__用来描述一个模块的属性

import 一个模块后，这个模块会被自动运行

'''

print(__doc__)


