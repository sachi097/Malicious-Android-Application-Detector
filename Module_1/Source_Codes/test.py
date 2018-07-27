from subprocess import Popen as out
import subprocess
import re
import os,shutil
import pandas

subprocess.call("py BFM.py")
subprocess.call("py BFB.py")

df=pandas.read_csv("outputBFM.csv")
pd=pandas.read_csv("outputBFB.csv")
ps=pandas.read_csv("class.csv")

arr=df.values
ayy=pd.values
axx=ps.values

name=arr[:,0:1]
resmal=arr[:,1:3]
classname=axx[:,1:2]

resben=ayy[:,1:3]

BFM=[]
BFB=[]

for i in range(len(resmal)):
    BFM.append(resmal[i])

for i in range(len(resben)):
    BFB.append(resben[i])

ds=open("Decision_Module.csv","w")
ds.write("Name,BFM,BFB,Decision_Module,Actual_Class\n")

un=0

for i in range(len(BFM)):
    bfm=list(BFM[i])
    bfm=bfm.index(1)
    bfb=list(BFB[i])
    bfb=bfb.index(1)
    if(bfm==0):
        if(bfm==bfb):
            ds.write(name[i][0]+",Malware,Malware,Malware,"+classname[i][0]+"\n")
        else:
            un+=1
            ds.write(name[i][0]+",Malware,Benign,Unclassified,"+classname[i][0]+"\n")
    else:
        if(bfm==bfb):
            ds.write(name[i][0]+",Benign,Benign,Benign,"+classname[i][0]+"\n")
        else:
            un+=1
            ds.write(name[i][0]+",Benign,Malware,Unclassified,"+classname[i][0]+"\n")
ds.close()

df=pandas.read_csv("Decision_Module.csv")
pandas.set_option("display.height",1000)
pandas.set_option("display.width",1000)
pandas.set_option("display.max_rows",275)
print(df)


bfmnbb,bfmnbm,bfmnmm,bfmnmb,accbfm,errbfm=0,0,0,0,0,0
bfbnbb,bfbnbm,bfbnmm,bfbnmb,accbfb,errbfb=0,0,0,0,0,0

m,b=0,0

azz=df.values

evameasure=azz[:,1:]

for i in range(len(evameasure)):
    if(evameasure[i][0]==evameasure[i][3]):
        if(evameasure[i][0]=="Malware"):
            bfmnmm+=1
            m+=1
        else:
            bfmnbb+=1
            b+=1
    else:
        if(evameasure[i][3]=="Benign" and evameasure[i][0]=="Malware"):
            bfmnbm+=1
            b+=1
        else:
            bfmnmb+=1
            m+=1
    if(evameasure[i][1]==evameasure[i][3]):
        if(evameasure[i][1]=="Malware"):
            bfbnmm+=1
        else:
            bfbnbb+=1
    else:
        if(evameasure[i][3]=="Benign" and evameasure[i][1]=="Malware"):
            bfbnbm+=1
        else:
            bfbnmb+=1

bfmtp=round((bfmnmm/(bfmnmm+bfmnmb))*100,0)
bfmtn=round((bfmnbb/(bfmnbb+bfmnbm))*100,0)
bfmfp=round((bfmnbm/(bfmnbb+bfmnbm))*100,0)
bfmfn=round((bfmnmb/(bfmnmm+bfmnmb))*100,0)

accbfm=round(((bfmnbb+bfmnmm)/(bfmnbb+bfmnbm+bfmnmb+bfmnmm))*100,0)
errbfm=round(((bfmnbm+bfmnmb)/(bfmnbb+bfmnbm+bfmnmb+bfmnmm))*100,0)

bfbtp=round((bfbnmm/(bfbnmm+bfbnmb))*100,0)
bfbtn=round((bfbnbb/(bfbnbb+bfbnbm))*100,0)
bfbfp=round((bfbnbm/(bfbnbb+bfbnbm))*100,0)
bfbfn=round((bfbnmb/(bfbnmm+bfbnmb))*100,0)

accbfb=round(((bfbnbb+bfbnmm)/(bfbnbb+bfbnbm+bfbnmb+bfbnmm))*100,0)
errbfb=round(((bfbnbm+bfbnmb)/(bfbnbb+bfbnbm+bfbnmb+bfbnmm))*100,0)

print("",end='\n\n')
print("Result Of BFM In % . Testing Sample - Benign : "+str(b)+", Malware : "+str(m))
print("             ---------------------",end='\n')
print("            |   Presicted Result  |",end='\n')
print("             ---------------------",end='\n')
print("            | Benign | Malicious  |",end='\n')
print(" ---------------------------------",end='\n')
print("| Benign    | "+str(bfmtn)+"   | "+str(bfmfp)+"       |",end='\n')
print(" ---------------------------------",end='\n')
print("| Malicious | "+str(bfmfn)+"   | "+str(bfmtp)+"       |",end='\n\n')
print(" ---------------------------------",end='\n\n\n')
print("Accuracy Of BFM : "+str(accbfm)+"% Error Of BFM : "+str(errbfm)+"%",end="\n\n")
print("-----------------------------------------------------------------------")


print("Result Of BFB In % . Testing Sample - Benign : "+str(b)+", Malware : "+str(m))
print("             ---------------------",end='\n')
print("            |   Predicted Result  |",end='\n')
print("             ---------------------",end='\n')
print("            | Benign | Malicious  |",end='\n')
print(" ---------------------------------",end='\n')
print("| Benign    | "+str(bfbtn)+"   | "+str(bfbfp)+"       |",end='\n')
print(" ---------------------------------",end='\n')
print("| Malicious | "+str(bfbfn)+"   | "+str(bfbtp)+"       |",end='\n')
print(" ---------------------------------",end='\n\n')
print("Accuracy Of BFB : "+str(accbfb)+" Error Of BFM : "+str(errbfb),end="\n\n")
print("-----------------------------------------------------------------------\n")

print("Total Samples : "+str(b+m)+" - Classified : "+str(b+m-un)+" Unclassified : "+str(un))
