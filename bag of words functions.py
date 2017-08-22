import glob
import os
import math
class bags(object):
    def __init__(self):
        pass
    def filetolist(f1,f2):
        f11=open(f1)
        f22=open(f2)
        f111=f11.read()
        f222=f22.read()
        a=f111.lower()
        b=f222.lower()
        l=a.split()
        k=b.split()
        return(l,k)
    def dictionary(l,k):
        dic1={}
        dic2={}
        for i in l:
            if i in dic1.keys():
                dic1[i]=dic1[i]+1
            else:
                dic1[i]=1
        #print("Freq of first Dictionary: ",dic1)
        #print("Freq of first Dictionary: ",dic1)
        for j in k:
            if j in dic2.keys():
                dic2[j]=dic2[j]+1
            else:
                dic2[j]=1
        return (dic1,dic2)
    def frequency(dic1,dic2):
        s=0
        sq1=0
        sq2=0
        temp=list(dic1.keys())+list(dic2.keys())
        temp1=[]
        for i  in temp:
            if i not in temp1:
                temp1.append(i)
                #print(temp1)
        for i in temp1:
            s=s+(dic1.get(i,0)*dic2.get(i,0))
        
        for i in dic1.values():
            sq1=sq1+pow(i,2)
            s1=math.sqrt(sq1)
        for j in dic2.values():
            sq2=sq2+pow(j,2)
            s2=math.sqrt(sq2)
            
        c=s/(s1*s2)
        #print(c*1005)
        return c
path=input("enter path of the directory to compare")
#path='C:\\Users\\Mr.Vijay Reddy\\Desktop\\project'
filelist=glob.glob(os.path.join(path,'*txt'))

for i in range(len(filelist)-1):
    
    for j in range((i+1),len(filelist)):
        
        (l,k)=bags.filetolist(filelist[i],filelist[j])
        (dic1,dic2)=bags.dictionary(l,k)
        k=bags.frequency(dic1,dic2)
        print("palagirism of ",os.path.basename(filelist[i]),os.path.basename(filelist[j]), "is",k*100)

