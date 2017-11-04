import sys

oridic={}
h = open("keitaiso3.csv")
lines = h.readlines()
for i in lines:
    i=i.split(" ")
    three=i[3].rstrip()
    oridic[i[0]]=(i[1],i[2],three)

k=1
menlist=[]
for i in range(1,30):
    for j in range(1,4000):
        templist=[]
        target=""
        number=str(i)+"_"+str(j)
        if number not in oridic:
            print(number)
            break
        else:
            tar = oridic[number]
        if not tar[0]=="":
            target+=tar[0]
        if not tar[1]=="":
            target+=tar[1]
        if not tar[2]=="":
            target+=tar[2]
        target=target.lstrip(",")
        templist=target.split(",")
        for l in templist:
            if not l in menlist:
                with open("feature1.csv", "a")as fo:
                    fo.write(str(k)+" "+l+"\n")
                k+=1
                menlist.append(l)