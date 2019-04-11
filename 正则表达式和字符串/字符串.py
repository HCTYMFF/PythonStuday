#格式化字符串
string="abc"
num=1.0
print("%s的值为%d"%(string,num))
print("%s的值为%.1f"%(string,num))
print("{0}的值为{1}".format(string,num))

world="version3.0"
print(world.center(20))#字符居中，若字符大于20个字符则正常显示，否则左右空格填充
print(world.center(20,"*"))#字符居中，若字符大于20个字符则正常显示，否则左右*填充
print(world.ljust(0))#字符左对齐
print(world.ljust(20))#字符左对齐，字符大小为20，若小于20，空格填充
print(world.ljust(20,"*"))#字符左对齐，字符大小为20，若小于20，*填充
print(world.rjust(20))
print(world.rjust(20,"*"))

#python中的不可见字符用\转义
print("hello\tworld")#\t代表tab
print(r"hello\tworld")#r表示不看转义字符，全部输出

#python内置函数 strip()、lstrip()、rstrip()可以去掉字符串中的转义字符
s="   \thello\tworld\nworld\n"
print(r"\thello\tworld\nworld\n.strip()=",s.strip())#去掉首尾的转义字符（和空格），中间的不管
print(r"\thello\tworld\nworld\n.lstrip()=",s.lstrip())#去掉左侧的转义字符（和空格），右侧和中间的不管
print(r"\thello\tworld\nworld\n.rstrip()=",s.rstrip())#去掉字符串右侧的转义字符（和空格），左侧和中间的不管

#字符串的合并
#python和java一样，用+进行字符串的链接，若左右都是字符串则链接，若都是数字则加，若类型不匹配，则报错
Str1="123"
Str2="456"
Str3=Str1+Str2
print(Str3)
strs=["a","b","c"]
print("".join(strs))#join配合列表实现多个字符串的链接

#字符串的截取
#通过切片可以取字串 [start:end:step]
strstr="hellowrold"
print(strstr[0:3:2])
sentence="boob said:,1,2,3,4"
print(sentence.split())#使用空格取子串
print(sentence.split(","))#使用逗号取字串
print(sentence.split(",",2))#使用逗号取字串，并且只取两个逗号，剩下的统一为一个子串


#字符串的比较
#python使用“==”和“！=比较两个字符串的大小”

bijiaostr=1
bijiaostr2="1"
#因为bijioastr1和bijiaostr2的字符类型不同所以两个比较的值不同
if bijiaostr==bijiaostr2:
    print("相同")
else:
    print("不相同")

if str(bijiaostr)==bijiaostr2:
    print("相同")
else:
    print("不相同")


#字串的比较
wordword="hello world"
print("wordword[0:5]==\"hello\"",wordword[0:5]=="hello")#字符串0-5字串内有 hello则返回true
print("wordword.startswith(\"hello\")",wordword.startswith("hello"))#字符串开始有hello则返回true
print("wordword.endswith(\"world\")",wordword.endswith("world"))#字符串尾部有world则返回true
print("wordword.endswith(\"ld\",6)",wordword.endswith("ld",6))#字符串倒数第一到倒数第六个数中间有ld则返回true
print("wordword.endswith(\"ld\",6,len(wordword))",wordword.endswith("ld",6,len(wordword)))#从6到字符串尾部有ld则返回true

#字符串的反转
def reverse(s):
    li=list(s)
    li.reverse()
    s="".join(li)
    return s

fanzhuan="我是一个兵"
print(reverse(fanzhuan))


#字符串的查找和替换

#python中使用find(左到右)和refind()（右到左）做查找
chazhao="hello wor;d"
print(chazhao.find("e"))
print(chazhao.rfind("w"))#从右往左查找w 出现的位置
print(chazhao[2:4].find("l"))#从字串中查找l

#字符串的替换
#python用replace 替换字符串
tihuan="YaoBeiTiHuanLe"
print(tihuan.replace("Yao","Buhuang"))#将字符串中的Yao替换为Buhuang
print(tihuan.replace("e","A"))#将字符串中的所有e替换为A
print(tihuan.replace("e","A",1))#将字符串中的e替换为A 仅仅替换第一个出现的e


#字符串 与日期的替换
import time,datetime

print(time.strftime("%Y-%m-%d %X %w  %W ",time.localtime()))#strftime可以实现从时间到字符串的转换
t=time.strptime("2018-8-8","%Y-%m-%d") #striptime函数将字符串变成一个元组
print(t)
a,b,c,d,e,f,g,h,i=t
print(a)
print(datetime.datetime(a,b,c,d,e,f))

print(time.time())