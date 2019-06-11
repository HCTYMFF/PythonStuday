#正则表达式的应用
'''
^代表正则的开始 $代表结束
\w 等于 字母数字下下划线
\W 匹配不是字母数字下划线
\s匹配空白字符
\d 匹配数字
\b匹配单词的开始和结束
. 匹配任意字符
[m]匹配单个字符
[m1m2m3m4m]匹配多个字符
[m-n]匹配区间内的数字和字母
（）对正则进行分组，一个圆括号表示一组
[^m] 匹配除m以外的字符串

* 匹配0次或者多次
+ 匹配1次或者多次
？ 匹配一次或者0次
{m} 重复m次
{m,n} 重复m到n次

[\(-]?  表示只能取 （和- 其中的一个，括号需要转义


martch(pattern,string,flag)#从字符串索引为0的地方匹配字符串,若从0开始匹配不到则返回None
search（pattern，string，flag）#在字符串中反复查找pattern规定的字符串，若全部匹配不到，则返回None
'''

import re
'''
re 模块学习
Python中字符串前面加上 r 表示原生字符串 不需要转义

1、match
re.match(pattern, string[, flags])  
从首字母开始开始匹配，string如果包含pattern子串，则匹配成功，返回Match对象，失败则返回None，若要完全匹配，pattern要以$结尾。

2、search
re.search(pattern, string[, flags])  
若string中包含pattern子串，则返回Match对象，否则返回None，注意，如果string中存在多个pattern子串，只返回第一个。

3、findall
re.findall(pattern, string[, flags])  
返回string中所有与pattern相匹配的全部字串，返回形式为数组。

4、finditer
re.finditer(pattern, string[, flags])  
返回string中所有与pattern相匹配的全部字串，返回形式为迭代器。

'''

s="hello World"
print(re.findall(r"^hello",s))
print(re.findall(r"world$",s))
print(re.findall(r"world$",s,re.I))
print(re.findall(r"\b\w+",s)) #匹配每个单词，输出 \b用来分割单词
print(re.sub("hello","hi",s))#sub替换函数，可以将字串进行替换,，替换成功输出替换成功的字符串
print(re.sub("hello","hi",s[-4:]))#替换失败输出原先被截取的字符串

print(re.subn(r"\s","*",s))#匹配结果多一个匹配成功的次数
print("匹配成功",re.subn(r"\s","*",s)[1],"次")
tel="(010)1234567"
tel1="101-1234567"
print(re.findall(r"[\(-]?[\d]{3}[\)-]?[\d]{7}",tel))
print(re.findall(r"[\(-]?[\d]{3}[\)-]?[\d]{7}",tel1))



#compile() 预编译正则表达式，加快查找效率
ss="123123132"
p=re.compile(r"\d+")  #pattern的属性 findall、finditer
print(p.findall(ss))
print(p.finditer(ss))