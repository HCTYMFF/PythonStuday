#将文件内容存入数组
import  io
import re
f=open("hello.txt","r")
list=[]
lines=f.readlines()

res=r"hello$"
for line in lines:
    line=line.strip()
    s=re.search(res,line)
    print (s)
    if(s==None):
        line=line+"hello"
        list.append(line)
    else:
        list.append(line)
f.close()
print(list)

f=open("aaa.123","r")
slist=f.read()
print(slist)
lll_array=[id for id in slist.split("\"") if len(id.strip())>0]
print(lll_array)
for id in lll_array:
    print("'"+id+"',",end=" ")
print("\n")
print(slist.split("\""))
f.close()

f=open("bbb.txt","r")
pphttps=r"^https://(\d{1,3}\.){3}(\d{1,3})"
pphttp=r"^http://(\d{1,3}\.){3}(\d{1,3})"
ppttt=r"(\d{1,3}\.){3}(\d{1,3})"
ppphttp=r"^(\d{1,3}\.){3}(\d{1,3})"

listtt=f.readlines()
abc=[]
for l in listtt:
  l=l.strip()
  if(l!=None):
    if(re.search(pphttp,l)):
        p=re.search(ppttt,l)
        p="https://"+p.group(0)
        abc.append(p)
    elif(re.search(ppphttp,l)):
        l="https://"+l
        abc.append(l)
    elif(re.search(pphttps,l)):
        abc.append(l)
    else:
        print(l,"不符合规则")
print(abc)
