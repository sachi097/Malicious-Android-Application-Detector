import re
import pandas 
import os
ds=open("sam.csv","w")
os.chdir("sample_testing/sam_xml")
cwd=os.getcwd()
print(cwd)
files=os.listdir()

mal_perm=["READ_SMS","WRITE_SMS","READ_PHONE_STATE","SEND_SMS","RECEIVE_SMS","WRITE_APN_SETTINGS","ACCESS_WIFI_STATE","RECEIVE_BOOT_COMPLETED","INSTALL_PACKAGES","CHANGE_WIFI_STATE","CALL_PHONE","RESTART_PACKAGES","READ_CONTACTS","WRITE_CONTACTS","DISABLE_KEYGUARD","READ_LOGS","SET_WALLPAPER","MOUNT_UNMOUNT_FILESYSTEMS","READ_HISTORY_BOOKMARKS","RECEIVE_WAP_PUSH","WRITE_HISTORY_BOOKMARKS","RECEIVE_MMS","WRITE_EXTERNAL_STORAGE","READ_EXTERNAL_STORAGE","GET_TASKS","DELETE_PACKAGES","CAMERA","PROCESS_OUTGOING_CALLS","ACCESS_LOCATION_EXTRA_COMMANDS","INTERNET"]
print(len(mal_perm))
ds.write("NAME,READ_SMS,WRITE_SMS,READ_PHONE_STATE,SEND_SMS,RECEIVE_SMS,WRITE_APN_SETTINGS,ACCESS_WIFI_STATE,RECEIVE_BOOT_COMPLETED,INSTALL_PACKAGES,CHANGE_WIFI_STATE,CALL_PHONE,RESTART_PACKAGES,READ_CONTACTS,WRITE_CONTACTS,DISABLE_KEYGUARD,READ_LOGS,SET_WALLPAPER,MOUNT_UNMOUNT_FILESYSTEMS,READ_HISTORY_BOOKMARKS,RECEIVE_WAP_PUSH,WRITE_HISTORY_BOOKMARKS,RECEIVE_MMS,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,GET_TASKS,DELETE_PACKAGES,CAMERA,PROCESS_OUTGOING_CALLS,ACCESS_LOCATION_EXTRA_COMMANDS,INTERNET\n")
c=0
for j in range(len(files)):
        c+=1
        print(files[j])
        bit_pattern = [0]*30
        for i in range(len(mal_perm)):
            pattern = re.compile(mal_perm[i], re.IGNORECASE)
            try:
                with open (files[j].replace(".apk",".xml"), 'rt') as in_file:        
                    for  linenum, line in enumerate(in_file): 
                        if pattern.search(line) != None:
                            bit_pattern[i]=1
            except FileNotFoundError:
                print("Log file not found.")
                
        ds.write((str(files[j].encode("utf-8")).replace(",","_").replace(".xml",".apk")+","+(str(bit_pattern).replace("[","").replace("]","")+"\n")).replace("b'","").replace("'",""))
ds.close()
print("SUCCESSFULLY FECTHED DATASET")
