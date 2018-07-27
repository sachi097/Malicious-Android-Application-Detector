from subprocess import Popen as out
import subprocess
import re
import os
cmd="py androaxml.py -i "
cwd=os.getcwd()
print(cwd)
extapk=(os.listdir())[4]
print(extapk)
os.chdir(extapk)
cwd=os.getcwd()
print(cwd)
files=os.listdir()
ds=open("dataset.csv","w")
mal_perm=["INTERNET","READ_PHONE_STATE","ACCESS_NETWORK_STATE","WRITE_EXTERNAL_STORAGE","READ_SMS","ACCESS_WIFI_STATE","RECEIVE_BOOT_COMPLETED","WRITE_SMS","SEND_SMS","RECEIVE_SMS","VIBRATE","ACCESS_COARSE_LOCATION","READ_CONTACTS","CALL_PHONE","ACCESS_FINE_LOCATION","WAKE_LOCK","WRITE_CONTACTS","CHANGE_WIFI_STATE","WRITE_APN_SETTINGS","RESTART_PACKAGES"]
ds.write("NAME,INTERNET,READ_PHONE_STATE,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_SMS,ACCESS_WIFI_STATE,RECEIVE_BOOT_COMPLETED,WRITE_SMS,SEND_SMS,RECEIVE_SMS,VIBRATE,ACCESS_COARSE_LOCATION,READ_CONTACTS,CALL_PHONE,ACCESS_FINE_LOCATION,WAKE_LOCK,WRITE_CONTACTS,CHANGE_WIFI_STATE,WRITE_APN_SETTINGS,RESTART_PACKAGES\n")
for j in range(len(files)):
    if(files[j]=="androaxml.py"):
        continue
    print(files[j])
    a=out(cmd+files[j],stdout=subprocess.PIPE)
    a,err=a.communicate()
    with open("f"+str(j)+".xml","wb") as f:
        f.write(a)
    bit_pattern = [0]*21
    for i in range(len(mal_perm)):
        pattern = re.compile(mal_perm[i], re.IGNORECASE)
        try:
            with open ("f"+str(j)+".xml", 'rt') as in_file:        
                for  linenum, line in enumerate(in_file): 
                    if pattern.search(line) != None:
                        bit_pattern[i]=1
        except FileNotFoundError:
            print("Log file not found.")
    ds.write(files[j]+str(bit_pattern).replace("[","").replace("]","")+"\n")
print("SUCCESSFULLY FECTHED DATASET")
ds.close()
