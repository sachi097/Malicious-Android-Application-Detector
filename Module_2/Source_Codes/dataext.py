from subprocess import Popen as out
import subprocess
import re
import os

ds=open("NBinputben.csv","w")
os.chdir("benign")#change to malware for extrating dataset of malware files and change at file open too
cwd=os.getcwd()
print(cwd)
files=os.listdir()
code_perm=["getSubscriberId","getDeviceId","getSimSerialNumber",".apk","chmod","abortBroadcast","intent.action.BOOT_COMPLETED","Runtime.exec()","/system/app","getLine1Number","/system/bin","createSubprocess","remount","DexclassLoader","getSimOperator","pm install","chown","getCallState","/system/bin/sh",".jar","mount","KeySpec","SMSReceiver","getNetworkOperator","SecretKey"]
manif_perm=["READ_SMS","WRITE_SMS","READ_PHONE_STATE","SEND_SMS","RECEIVE_SMS","WRITE_APN_SETTINGS","ACCESS_WIFI_STATE","RECEIVE_BOOT_COMPLETED","INSTALL_PACKAGES","CHANGE_WIFI_STATE","CALL_PHONE","RESTART_PACKAGES","READ_CONTACTS","WRITE_CONTACTS","DISABLE_KEYGUARD","READ_LOGS","SET_WALLPAPER","MOUNT_UNMOUNT_FILESYSTEMS","READ_HISTORY_BOOKMARKS","RECEIVE_WAP_PUSH","WRITE_HISTORY_BOOKMARKS","RECEIVE_MMS","WRITE_EXTENAL_STORAGE","READ_EXTERNAL_STORAGE","GET_TASKS","DELETE_PACKAGES","CAMERA","PROCESS_OUTGOING_CALLS","ACCESS_LOCATION_EXTRA_COMMANDS","INTERNET"]
ds.write("Name,READ_SMS,WRITE_SMS,READ_PHONE_STATE,SEND_SMS,RECEIVE_SMS,WRITE_APN_SETTINGS,ACCESS_WIFI_STATE,RECEIVE_BOOT_COMPLETED,INSTALL_PACKAGES,CHANGE_WIFI_STATE,CALL_PHONE,RESTART_PACKAGES,READ_CONTACTS,WRITE_CONTACTS,DISABLE_KEYGUARD,READ_LOGS,SET_WALLPAPER,MOUNT_UNMOUNT_FILESYSTEMS,READ_HISTORY_BOOKMARKS,RECEIVE_WAP_PUSH,WRITE_HISTORY_BOOKMARKS,RECEIVE_MMS,WRITE_EXTENAL_STORAGE,READ_EXTERNAL_STORAGE,GET_TASKS,DELETE_PACKAGES,CAMERA,PROCESS_OUTGOING_CALLS,ACCESS_LOCATION_EXTRA_COMMANDS,INTERNET,getSubscriberId,getDeviceId,getSimSerialNumber,.apk,chmod,abortBroadcast,intent.action.BOOT_COMPLETED,Runtime.exec(),/system/app,getLine1Number,/system/bin,createSubprocess,remount,DexclassLoader,getSimOperator,pm install,chown,getCallState,/system/bin/sh,.jar,mount,KeySpec,SMSReceiver,getNetworkOperator,SecretKey\n")
for j in range(len(files)):
    ext=os.path.splitext(files[j])[1]
    if(ext==".apk"):
        print(files[j])
        bit_pattern = [0]*55
        a=out("java -jar baksmali.jar dump "+files[j],stdout=subprocess.PIPE)
        a,err=a.communicate()
        with open(cwd+"/smali_ben/"+str(files[j]).replace(".apk","")+".txt","wb") as f:
            f.write(a)
        for i in range(len(manif_perm+code_perm)):
            if(i<30):
                pattern = re.compile(manif_perm[i], re.IGNORECASE)
                with open (cwd+"/ben_xml/"+str(files[j]).replace(".apk","")+".xml", 'rt') as in_file:        
                    for  linenum, line in enumerate(in_file): 
                        if pattern.search(line) != None:
                            bit_pattern[i]=1
            else:
                pattern = re.compile(code_perm[i-30], re.IGNORECASE)
                with open (cwd+"/smali_ben/"+str(files[j]).replace(".apk","")+".txt", 'rt') as in_file:        
                    for  linenum, line in enumerate(in_file):
                        if pattern.search(line) != None:
                            bit_pattern[i]=1
        print(j)
        ds.write((str(files[j].encode("utf-8")).replace(",","_")+","+(str(bit_pattern).replace("[","").replace("]","")+"\n")).replace("b'","").replace("'","")) 
print("SUCCESSFULLY FECTHED DATASET")
ds.close()


        
 
