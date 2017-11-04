import sys

oridic={}
h = open("keitaiso4.csv")
lines = h.readlines()
for i in lines:
    i=i.split(" ")
    three=i[3].rstrip()
    oridic[i[0]]=(i[1],i[2],three)

k=1
temp=[]
menlist={}
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
        temp.append(templist)
        for l in templist:
            if l not in menlist:
                #with open("featurekai.csv", "a")as fo:
                #    fo.write(str(k)+" "+l+"\n")
                menlist[l]=1
            else:
                menlist[l]+=1

memo=[]
for i in list(menlist):
    if menlist[i]==1:
        menlist.pop(i)
    elif menlist[i]>5000:
        print(i)
        menlist.pop(i)
for i in temp:
    for j in i:
        if j in menlist and not j in memo:
            with open("feature4.csv", "a")as fo:
                fo.write(str(k)+" "+j+"\n")
            memo.append(j)
            k+=1