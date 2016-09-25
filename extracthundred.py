import random
f=open("data100.csv","r")
data = f.read()
g=open("data100types.js","w")
d = data.splitlines()
for i in range(len(d)):
    d[i] = d[i].split(',')
g.write("[")
for i in range(100):
    g.write("{lat:"+d[i][1]+",long:"+d[i][2]+",type:'"+d[i][3]+"'}")
    g.write(",\n")
g.write("]")
g.close()
f.close()
