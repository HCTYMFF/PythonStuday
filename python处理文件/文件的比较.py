'''
python 提供了difflib模块的seqenceMatcher(None,a,b)类实现连个文件的比较
创建比较对象以a作为参考对象
其中get_opcedes()可以返回比较结果
get_codes()方法返回一个元祖（tag,i1,i2,j1,j2）
replace a[i1:i2]被[j1:j2]替换
Delete a[i1:i2] 分片被删除，此时j1=j2
equal a[i1:i2]等于b[j1:j2]
insert b[j1:j2]插入a[i1:i2]位置处，此时的i1等于i2
'''
import difflib,os
path="C:\\Users\\Administrator\\Desktop\\1.txt"
path2="C:\\Users\\Administrator\\Desktop\\2.txt"
f1=open(path)
f2=open(path2)
src=f1.read()
dst=f2.read()
s=difflib.SequenceMatcher(lambda x:x=="",src,dst) #x==""表示忽略换行
#s=difflib.SequenceMatcher(src,dst) #x==""表示忽略换行
for tag,i1,i2,j1,j2 in s.get_opcodes():
    #print(type(i1))
    #if tag=="replace":
        print("%s src[%d:%d]=%s des[%d:%d]=%s"%(tag,i1,i2,src[i1:i2],j1,j2,dst[j1:j2]))
f1.close()
f2.close()
os.startfile(path)
os.startfile(path2)