import pandas
import os,subprocess
from subprocess import Popen as out
import re

ds=open("code.csv","w")
df=pandas.read_csv('Decision_Module.csv')
arr=df.values
y=['']*143
z=[0]*143
x=arr[:,:]
j=0
for i in x:
    if(i[3]=="Unclassified"):
        y[j]=i[0]
        if(i[4]=="Malware"):
            z[j]=1
        j+=1
y=y[:-1]
os.chdir('sample_testing')
files=os.listdir()
cwd=os.getcwd()
print(cwd)
code_perm=["getSubscriberId","getDeviceId","getSimSerialNumber",".apk","chmod","abortBroadcast","intent.action.BOOT_COMPLETED","Runtime.exec()","/system/app","getLine1Number","/system/bin","createSubprocess","remount","DexclassLoader","getSimOperator","pm install","chown","getCallState","/system/bin/sh",".jar","mount","KeySpec","SMSReceiver","getNetworkOperator","SecretKey"]
ds.write("Name,getSubscriberId,getDeviceId,getSimSerialNumber,.apk,chmod,abortBroadcast,intent.action.BOOT_COMPLETED,Runtime.exec(),/system/app,getLine1Number,/system/bin,createSubprocess,remount,DexclassLoader,getSimOperator,pm install,chown,getCallState,/system/bin/sh,.jar,mount,KeySpec,SMSReceiver,getNetworkOperator,SecretKey,class\n")
c=0
for j in range(len(files)):
    ext=os.path.splitext(files[j])[1]
    if(ext==".apk"):
        print(files[j])
        bit_pattern = [0]*25
        c+=1
        if(files[j] in y):
            try:
                for i in range(len(code_perm)):
                    pattern = re.compile(code_perm[i], re.IGNORECASE)
                    with open (cwd+"/smali_sam/"+str(files[j]).replace(".apk","")+".txt", 'rt') as in_file:        
                        for  linenum, line in enumerate(in_file):
                            if pattern.search(line) != None:
                                bit_pattern[i]=1
            except:
                bit_pattern=0
        else:
            a=out("java -jar baksmali.jar dump "+files[j],stdout=subprocess.PIPE)
            a,err=a.communicate()
            with open(cwd+"/smali_sam/"+str(files[j]).replace(".apk","")+".txt","wb") as f:
                f.write(a)
            for i in range(len(code_perm)):
                pattern = re.compile(code_perm[i], re.IGNORECASE)
                with open (cwd+"/smali_sam/"+str(files[j]).replace(".apk","")+".txt", 'rt') as in_file:        
                    for  linenum, line in enumerate(in_file):
                        if pattern.search(line) != None:
                            bit_pattern[i]=1
        print(bit_pattern)
        print(c)
        ds.write((str(files[j].encode("utf-8")).replace(",","_")+","+(str(bit_pattern).replace("[","").replace("]","")+"\n")).replace("b'","").replace("'",""))
ds.close()

