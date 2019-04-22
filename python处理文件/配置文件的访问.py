'''
windows的ini文件就是一种传统的配置文件
ini文件由多个块组成，每个块由多个配置项组成
python通过configparser模块用于解析配置文件configparaser模块的ConfigParser类可读取ini文件的内容
parser是解析器的意思
'''
#配置文件的读取
import configparser
config=configparser.ConfigParser()
config.read("test.ini")
sections=config.sections() #返回所有配置块
print("配置块",sections) #输出所有配置快
o=config.options("AAA") #返回配置快AAA的所有配置项
print("配置项",o)
v=config.items("AAA")#返配置块AAA的所有内容
print("配置内容",v)
access=config.get("AAA","a1")#返回配置块AAA下配置项a1下的配置内容
print(access)

'''
#配置文件的写入
config.add_section("HHH")
config.set("HHH","h1","111")
f=open("test.ini","w+") #在写配置文件的时候，会把原先的配置文件读入在将新的加入，最后写入文件，so不能用a+
config.write(f)
f.close()
'''

#配置文件的修改
configerer=configparser.ConfigParser()
configerer.read("test.ini")
configerer.set("HHH","h1","123")#将HHH h1的值改为123
f=open("test.ini","r+")
configerer.write(f)
f.close()


#删除配置项  删除可以使用remove_option()删除配置项下的配置快，remove_sections()可以删除配置块

configerer.read("test.ini")
configerer.remove_section("GGG")  #删除配置快，会把配置快下的配置项一起删除
configerer.remove_option("III","i1") #删除配置项，指定配置快下的某一配置项删除
f=open("test.ini","w+")
configerer.write(f)
f.close()




