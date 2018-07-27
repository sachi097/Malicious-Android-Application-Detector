from subprocess import call
import matplotlib.pyplot as plt
import pandas as pd


print("Permission-Based Model")

call("py NBper.py 6")
call("py NBper.py 11")
call("py NBper.py 16")
call("py NBper.py 21")
call("py NBper.py 31")


print("Code-Based Model")

call("py NBcode.py 6")
call("py NBcode.py 11")
call("py NBcode.py 16")
call("py NBcode.py 21")
call("py NBcode.py 26")

print("Mixed-Based Model")

call("py NBmixed.py 6")
call("py NBmixed.py 11")
call("py NBmixed.py 16")
call("py NBmixed.py 21")
call("py NBmixed.py 26")


print("Plotting Graphs")

df=pd.read_csv("outputNBcode6.csv")
arr=df.values

da=pd.read_csv("outputNBcode11.csv")
ayy=da.values

db=pd.read_csv("outputNBcode16.csv")
aee=db.values

dc=pd.read_csv("outputNBcode21.csv")
aff=dc.values

dd=pd.read_csv("outputNBcode26.csv")
agg=dd.values

dg=pd.read_csv("outputNBper6.csv")
ahh=dg.values

dh=pd.read_csv("outputNBper11.csv")
aii=dh.values

di=pd.read_csv("outputNBper16.csv")
ajj=di.values

dj=pd.read_csv("outputNBper21.csv")
akk=dj.values

dk=pd.read_csv("outputNBper31.csv")
ass=dk.values

dl=pd.read_csv("outputNBmixed6.csv")
amm=dl.values

dm=pd.read_csv("outputNBmixed11.csv")
ann=dm.values

dn=pd.read_csv("outputNBmixed16.csv")
aoo=dn.values

do=pd.read_csv("outputNBmixed21.csv")
app=do.values

dp=pd.read_csv("outputNBmixed26.csv")
aqq=dp.values


x1 = [4,9,14,19,24]
x2 = [5,10,15,20,25]
x3 = [6,11,16,21,26]

y6=ahh[0]
y1=arr[0]
y11=amm[0]

y7=aii[0]
y2=ayy[0]
y12=ann[0]

y8=ajj[0]
y3=aee[0]
y13=aoo[0]

y9=akk[0]
y4=aff[0]
y14=app[0]

y10=ass[0]
y5=agg[0]
y15=aqq[0]



yacc=[[y6[0],y7[0],y8[0],y9[0],y10[0]],[y1[0],y2[0],y3[0],y4[0],y5[0]],[y11[0],y12[0],y13[0],y14[0],y15[0]]]
yerr=[[y6[1],y7[1],y8[1],y9[1],y10[1]],[y1[1],y2[1],y3[1],y4[1],y5[1]],[y11[1],y12[1],y13[1],y14[1],y15[1]]]
ytp=[[y6[2],y7[2],y8[2],y9[2],y10[2]],[y1[2],y2[2],y3[2],y4[2],y5[2]],[y11[2],y12[2],y13[2],y14[2],y15[2]]]
ytn=[[y6[3],y7[3],y8[3],y9[3],y10[3]],[y1[3],y2[3],y3[3],y4[3],y5[3]],[y11[3],y12[3],y13[3],y14[3],y15[3]]]
yfp=[[y6[4],y7[4],y8[4],y9[4],y10[4]],[y1[4],y2[4],y3[4],y4[4],y5[4]],[y11[4],y12[4],y13[4],y14[4],y15[4]]]
yfn=[[y6[5],y7[5],y8[5],y9[5],y10[5]],[y1[5],y2[5],y3[5],y4[5],y5[5]],[y11[5],y12[5],y13[5],y14[5],y15[5]]]
yp=[[y6[6],y7[6],y8[6],y9[6],y10[6]],[y1[6],y2[6],y3[6],y4[6],y5[6]],[y11[6],y12[6],y13[6],y14[6],y15[6]]]
yr=[[y6[7],y7[7],y8[7],y9[7],y10[7]],[y1[7],y2[7],y3[7],y4[7],y5[7]],[y11[7],y12[7],y13[7],y14[7],y15[7]]]




ax=plt.subplot(111)
plt.title("Accuracy")
plt.xlabel("Number Of Features (n)")
plt.ylabel("Percentage (%) ")
ax.bar(x1,yacc[0],label="Permission")
ax.bar(x2,yacc[1],label="Code")
ax.bar(x3,yacc[2],label="Mixed")
draw= ax.get_position()
ax.set_position([draw.x0,draw.y0,draw.width*0.9,draw.height])
ax.legend(loc="upper center",bbox_to_anchor=(1.13,0.8),shadow=True,ncol=1)
plt.show()

ax=plt.subplot(111)
plt.title("Error")
plt.xlabel("Number Of Features (n)")
plt.ylabel("Percentage (%) ")
ax.bar(x1,yerr[0],label="Permission")
ax.bar(x2,yerr[1],label="Code")
ax.bar(x3,yerr[2],label="Mixed")
draw= ax.get_position()
ax.set_position([draw.x0,draw.y0,draw.width*0.9,draw.height])
ax.legend(loc="upper center",bbox_to_anchor=(1.13,0.8),shadow=True,ncol=1)
plt.show()

ax=plt.subplot(111)
plt.title("True Positive")
plt.xlabel("Number Of Features (n)")
plt.ylabel("Percentage (%) ")
ax.bar(x1,ytp[0],label="Permission")
ax.bar(x2,ytp[1],label="Code")
ax.bar(x3,ytp[2],label="Mixed")
draw= ax.get_position()
ax.set_position([draw.x0,draw.y0,draw.width*0.9,draw.height])
ax.legend(loc="upper center",bbox_to_anchor=(1.13,0.8),shadow=True,ncol=1)
plt.show()

ax=plt.subplot(111)
plt.title("True Negative")
plt.xlabel("Number Of Features (n)")
plt.ylabel("Percentage (%) ")
ax.bar(x1,ytn[0],label="Permission")
ax.bar(x2,ytn[1],label="Code")
ax.bar(x3,ytn[2],label="Mixed")
draw= ax.get_position()
ax.set_position([draw.x0,draw.y0,draw.width*0.9,draw.height])
ax.legend(loc="upper center",bbox_to_anchor=(1.13,0.8),shadow=True,ncol=1)
plt.show()

ax=plt.subplot(111)
plt.title("False Positive")
plt.xlabel("Number Of Features (n)")
plt.ylabel("Percentage (%) ")
ax.bar(x1,yfp[0],label="Permission")
ax.bar(x2,yfp[1],label="Code")
ax.bar(x3,yfp[2],label="Mixed")
draw= ax.get_position()
ax.set_position([draw.x0,draw.y0,draw.width*0.9,draw.height])
ax.legend(loc="upper center",bbox_to_anchor=(1.13,0.8),shadow=True,ncol=1)
plt.show()

ax=plt.subplot(111)
plt.title("False Negative")
plt.xlabel("Number Of Features (n)")
plt.ylabel("Percentage (%) ")
ax.bar(x1,yfn[0],label="Permission")
ax.bar(x2,yfn[1],label="Code")
ax.bar(x3,yfn[2],label="Mixed")
draw= ax.get_position()
ax.set_position([draw.x0,draw.y0,draw.width*0.9,draw.height])
ax.legend(loc="upper center",bbox_to_anchor=(1.13,0.8),shadow=True,ncol=1)
plt.show()

ax=plt.subplot(111)
plt.title("Precision")
plt.xlabel("Number Of Features (n)")
plt.ylabel("Percentage (%) ")
ax.bar(x1,yp[0],label="Permission")
ax.bar(x2,yp[1],label="Code")
ax.bar(x3,yp[2],label="Mixed")
draw= ax.get_position()
ax.set_position([draw.x0,draw.y0,draw.width*0.9,draw.height])
ax.legend(loc="upper center",bbox_to_anchor=(1.13,0.8),shadow=True,ncol=1)
plt.show()

ax=plt.subplot(111)
plt.title("Recall")
plt.xlabel("Number Of Features (n)")
plt.ylabel("Percentage (%) ")
ax.bar(x1,yr[0],label="Permission")
ax.bar(x2,yr[1],label="Code")
ax.bar(x3,yr[2],label="Mixed")
draw= ax.get_position()
ax.set_position([draw.x0,draw.y0,draw.width*0.9,draw.height])
ax.legend(loc="upper center",bbox_to_anchor=(1.13,0.8),shadow=True,ncol=1)
plt.show()
