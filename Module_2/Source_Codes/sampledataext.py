import pandas
import os,subprocess
from subprocess import Popen as out
import re

ds=open("NBinputsam.csv","w")
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
os.chdir('sample_testing')
files=os.listdir()
cwd=os.getcwd()
print(cwd)
code_perm=["getSubscriberId","getDeviceId","getSimSerialNumber",".apk","chmod","abortBroadcast","intent.action.BOOT_COMPLETED","Runtime.exec()","/system/app","getLine1Number","/system/bin","createSubprocess","remount","DexclassLoader","getSimOperator","pm install","chown","getCallState","/system/bin/sh",".jar","mount","KeySpec","SMSReceiver","getNetworkOperator","SecretKey"]
manif_perm=["READ_SMS","WRITE_SMS","READ_PHONE_STATE","SEND_SMS","RECEIVE_SMS","WRITE_APN_SETTINGS","ACCESS_WIFI_STATE","RECEIVE_BOOT_COMPLETED","INSTALL_PACKAGES","CHANGE_WIFI_STATE","CALL_PHONE","RESTART_PACKAGES","READ_CONTACTS","WRITE_CONTACTS","DISABLE_KEYGUARD","READ_LOGS","SET_WALLPAPER","MOUNT_UNMOUNT_FILESYSTEMS","READ_HISTORY_BOOKMARKS","RECEIVE_WAP_PUSH","WRITE_HISTORY_BOOKMARKS","RECEIVE_MMS","WRITE_EXTENAL_STORAGE","READ_EXTERNAL_STORAGE","GET_TASKS","DELETE_PACKAGES","CAMERA","PROCESS_OUTGOING_CALLS","ACCESS_LOCATION_EXTRA_COMMANDS","INTERNET"]
ds.write("Name,READ_SMS,WRITE_SMS,READ_PHONE_STATE,SEND_SMS,RECEIVE_SMS,WRITE_APN_SETTINGS,ACCESS_WIFI_STATE,RECEIVE_BOOT_COMPLETED,INSTALL_PACKAGES,CHANGE_WIFI_STATE,CALL_PHONE,RESTART_PACKAGES,READ_CONTACTS,WRITE_CONTACTS,DISABLE_KEYGUARD,READ_LOGS,SET_WALLPAPER,MOUNT_UNMOUNT_FILESYSTEMS,READ_HISTORY_BOOKMARKS,RECEIVE_WAP_PUSH,WRITE_HISTORY_BOOKMARKS,RECEIVE_MMS,WRITE_EXTENAL_STORAGE,READ_EXTERNAL_STORAGE,GET_TASKS,DELETE_PACKAGES,CAMERA,PROCESS_OUTGOING_CALLS,ACCESS_LOCATION_EXTRA_COMMANDS,INTERNET,getSubscriberId,getDeviceId,getSimSerialNumber,.apk,chmod,abortBroadcast,intent.action.BOOT_COMPLETED,Runtime.exec(),/system/app,getLine1Number,/system/bin,createSubprocess,remount,DexclassLoader,getSimOperator,pm install,chown,getCallState,/system/bin/sh,.jar,mount,KeySpec,SMSReceiver,getNetworkOperator,SecretKey,class\n")
c=0
for j in range(len(y)):
    if(y[j] in files):
        c+=1
        print(y[j])
        bit_pattern = [0]*55
        a=out("java -jar baksmali.jar dump "+y[j],stdout=subprocess.PIPE)
        a,err=a.communicate()
        with open(cwd+"/smali_sam/"+str(y[j]).replace(".apk","")+".txt","wb") as f:
            f.write(a)
        for i in range(len(manif_perm+code_perm)):
            if(i<30):
                pattern = re.compile(manif_perm[i], re.IGNORECASE)
                with open (cwd+"/sam_xml/"+str(y[j]).replace(".apk","")+".xml", 'rt') as in_file:        
                    for  linenum, line in enumerate(in_file): 
                        if pattern.search(line) != None:
                            bit_pattern[i]=1
            else:
                pattern = re.compile(code_perm[i-30], re.IGNORECASE)
                with open (cwd+"/smali_sam/"+str(y[j]).replace(".apk","")+".txt", 'rt') as in_file:        
                    for  linenum, line in enumerate(in_file):
                        if pattern.search(line) != None:
                            bit_pattern[i]=1
        print(c)
        ds.write((str(y[j].encode("utf-8")).replace(",","_")+","+(str(bit_pattern).replace("[","").replace("]","")+","+str(z[j])+"\n")).replace("b'","").replace("'",""))
ds.close()
