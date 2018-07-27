from subprocess import Popen as out
import subprocess
import re
import os,shutil
cmd="py androaxml.py -i "
os.chdir("benign")
cwd=os.getcwd()
print(cwd)
files=os.listdir()
ds=open("dataset1.csv","w")
ben_perm=["INTERNET","ACCESS_NETWORK_STATE","WRITE_EXTERNAL_STORAGE","READ_PHONE_STATE","VIBRATE","ACCESS_COARSE_LOCATION","WAKE_LOCK","ACCESS_FINE_LOCATION","RECEIVE_BOOT_COMPLETED","ACCESS_WIFI_STATE","READ_CONTACTS","WRITE_SETTINGS","GET_ACCOUNTS","CAMERA","CALL_PHONE","WRITE_CONTACTS","GET_TASKS","RECORD_AUDIO","READ_HISTORY_BOOKMARKS","WRITE_HISTORY_BOOKMARKS"]
ds.write("NAME,INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_PHONE_STATE,VIBRATE,ACCESS_COARSE_LOCATION,WAKE_LOCK,ACCESS_FINE_LOCATION,RECEIVE_BOOT_COMPLETED,ACCESS_WIFI_STATE,READ_CONTACTS,WRITE_SETTINGS,GET_ACCOUNTS,CAMERA,CALL_PHONE,WRITE_CONTACTS,GET_TASKS,RECORD_AUDIO,READ_HISTORY_BOOKMARKS,WRITE_HISTORY_BOOKMARKS\n")
for j in range(len(files)):
    ext=os.path.splitext(files[j])[1]
    if(ext==".apk"):
        print(files[j])
        a=out(cmd+files[j],stdout=subprocess.PIPE)
        a,err=a.communicate()
        with open(str(files[j]).replace(".apk","")+".xml","wb") as f:
            f.write(a)
        bit_pattern = [0]*20
        for i in range(len(ben_perm)):
            pattern = re.compile(ben_perm[i], re.IGNORECASE)
            try:
                with open (str(files[j]).replace(".apk","")+".xml", 'rt') as in_file:        
                    for  linenum, line in enumerate(in_file): 
                        if pattern.search(line) != None:
                            bit_pattern[i]=1
            except FileNotFoundError:
                print("Log file not found.")
        dst=os.getcwd()+"/ben_xml/"+str(files[j]).replace(".apk","")+".xml"
        src=os.getcwd()+"/"+str(files[j]).replace(".apk","").replace("b'","").replace("'","")+".xml"
        shutil.move(src,dst)
        ds.write((str(files[j].encode("utf-8")).replace(",","_")+","+(str(bit_pattern).replace("[","").replace("]","")+"\n")).replace("b'","").replace("'",""))
print("SUCCESSFULLY FECTHED DATASET")
ds.close()
os.chdir("..")
src=os.getcwd()+"/benign/dataset1.csv"
dst=os.getcwd()
shutil.move(src,dst)
