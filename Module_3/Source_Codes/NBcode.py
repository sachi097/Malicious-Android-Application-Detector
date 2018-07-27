import pandas as pd
import numpy as np
from collections import Counter, defaultdict
import sys

def occurrences(list1):
    no_of_examples = len(list1)
    prob = dict(Counter(list1))    
    for key in prob.keys():
        prob[key] = prob[key] / float(no_of_examples)
    return prob

def naive_bayes(training, outcome, new_sample,classlabel):
    classes     = np.unique(outcome)
    rows, cols  = np.shape(training)

    likelihoods = {}
    for cls in classes:
        likelihoods[cls] = defaultdict(list)
 
    class_probabilities = occurrences(outcome)
 
    for cls in classes:
        row_indices = np.where(outcome == cls)[0]
        subset = training[row_indices, : ]
        r, c = np.shape(subset)
        for j in range(0,c):
            likelihoods[cls][j] += list(subset[:,j])
 
    for cls in classes:
        for j in range(0,cols):
             likelihoods[cls][j] = occurrences(likelihoods[cls][j])
 
 
    results = {}
    bb,bm,mb,mm=0,0,0,0
    tp,tn,fp,fn=0,0,0,0
    q=[]
    for i in range(0,len(new_sample)):
        for cls in classes:
            class_probability = class_probabilities[cls]
            for j in range(len(new_sample[i])):
                relative_values = likelihoods[cls][j]
                if new_sample[i][j] in relative_values.keys():
                    class_probability *= relative_values[new_sample[i][j]]
                else:
                    class_probability *= 0
            results[cls] = class_probability
        print (results)
        if(results[0]>results[1]):
            t=0
        else:
            t=1
        if(t==0):
            if(t==classlabel[i]):
                print(t,classlabel[i])
                bb+=1
            else:
                print(t,classlabel[i])
                mb+=1
        else:
            if(t==classlabel[i]):
                print(t,classlabel[i])
                mm+=1
            else:
                print(t,classlabel[i])
                bm+=1

    tp,tn,fp,fn=0,0,0,0
    tp=round((((mm)/(mb+mm)))*100,0)
    tn=round((((bb)/(bb+bm)))*100,0)
    fp=round((((bm)/(bb+bm)))*100,0)
    fn=round((((mb)/(mb+mm)))*100,0)
    acc=round((((bb+mm)/(bb+bm+mb+mm)))*100,0)
    err=round(((bm+mb)/(bb+bm+mb+mm))*100,0)
    p=round(((mm)/(bm+mm))*100,0)
    r=round(((bb)/(mb+bb))*100,0)
    print("Result Of NB In % . Testing Sample - Benign : "+str(bb+bm)+", Malware : "+str(mm+mb))
    print("             ---------------------",end='\n')
    print("            |   Predicted Result  |",end='\n')
    print("             ---------------------",end='\n')
    print("            | Benign | Malicious  |",end='\n')
    print(" ---------------------------------",end='\n')
    print("| Benign    | "+str(tn)+"   | "+str(fp)+"       |",end='\n')
    print(" ---------------------------------",end='\n')
    print("| Malicious | "+str(fn)+"   | "+str(tp)+"       |",end='\n')
    print(" ---------------------------------",end='\n\n')
    print("-----------------------------------------------------------------------\n")
    print("Classification : "+str(acc)+"% Missclassification : "+str(err)+"%")
    ds=open("outputNBcode"+str(sys.argv[1])+".csv","w")
    ds.write("Acc,Err,tp,tn,fp,fn,p,r\n")
    ds.write(str(acc)+","+str(err)+","+str(tp)+","+str(tn)+","+str(fp)+","+str(fn)+","+str(p)+","+str(r)+"\n")
    ds.close()
        
 
if __name__ == "__main__":
    df = pd.read_csv('code.csv')
    arr = df.values
    d=sys.argv[1]
    d=int(d)
    x=arr[:1068,1:d]
    y=arr[-262:,1:d]
    z=arr[-262:,-1:]
    training   = np.asarray(x)
    classlabel = np.asarray(z)
    outcome    = np.asarray([1]*522+[0]*546)
    new_sample = np.asarray(y)
    naive_bayes(training, outcome, new_sample,classlabel)
