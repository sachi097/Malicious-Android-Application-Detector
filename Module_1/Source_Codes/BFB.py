import fnv
import xxhash
import mmh3 as m
import pandas

df=pandas.read_csv("dataset1.csv")
pd=pandas.read_csv("sampleBFB.csv")
arr=df.values
ayy=pd.values
train=[]
test=[]
x=arr[:,1:21]
p=ayy[:,0:21]
z=ayy[:,1:21]
for i in range(len(x)):
    train.append(x[i])

for i in range(len(z)):
    test.append(z[i])

BFB=[0]*2381

for i in range(len(train)):
    y=xxhash.xxh32()
    y.update(str(train[i]))
    h1=y.intdigest()%794
    h2=m.hash(str(train[i]))%794
    h3=(fnv.hash(train[i],algorithm=fnv.fnv_1a,bits=64))%793
    BFB[h1]=1
    BFB[h2+794]=1
    BFB[h3+1588]=1
    
ds=open("outputBFB.csv","w")
ds.write("NAME,MALWARE,BEGING\n")
for i in range(len(test)):
    mal=0
    ben=0
    y=xxhash.xxh32()
    y.update(str(test[i]))
    h1=y.intdigest()%794
    h2=m.hash(str(test[i]))%794
    h3=(fnv.hash(test[i],algorithm=fnv.fnv_1a,bits=64))%793
    if(BFB[h1]==1 and BFB[h2+794]==1 and BFB[h3+1588]==1):
        ben=1
    else:
        mal=1
    ds.write(p[i][0]+","+str(mal)+","+str(ben)+"\n")
ds.close()



