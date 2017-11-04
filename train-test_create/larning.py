import sys
import multiprocessing as mp

oridic={}
h = open("keitaiso.csv")
lines = h.readlines()
for i in lines:
    i=i.split(" ")
    three=i[3].rstrip()
    oridic[i[0]]=(i[1],i[2],three)
h.close()
feadic={}
h = open("feature.csv")
lines = h.readlines()
for i in lines:
    i=i.split(" ")
    three=i[1].rstrip()
    feadic[three]=i[0]
h.close()

def cul(start,ends,odic,fdic):
    kekka=[]
    kekka2=[]
    for i in range(start,ends):
        k=0
        for j in range(1,4000):
            vecdic2={}
            vecdic={}
            if i ==1:
                if j >50:
                    k=1
            if i ==2:
                if j >389:
                    k=1
            if i ==3:
                if j >139:
                    k=1
            if i ==4:
                if j >90:
                    k=1
            if i ==5:
                if j >27:
                    k=1
            if i ==6:
                if j >87:
                    k=1
            if i ==7:
                if j >206:
                    k=1
            if i ==8:
                if j >47:
                    k=1
            if i ==9:
                if j >49:
                    k=1
            if i ==10:
                if j >293:
                    k=1
            if i ==11:
                if j >83:
                    k=1
            if i ==12:
                if j >37:
                    k=1
            if i ==13:
                if j >119:
                    k=1
            if i ==14:
                if j >58:
                    k=1
            if i ==15:
                if j >64:
                    k=1
            if i ==16:
                if j >15:
                    k=1
            if i ==17:
                if j >227:
                    k=1
            if i ==18:
                if j >66:
                    k=1
            if i ==19:
                if j >33:
                    k=1
            if i ==20:
                if j >88:
                    k=1
            if i ==21:
                if j >72:
                    k=1
            if i ==22:
                if j >93:
                    k=1
            if i ==23:
                if j >46:
                    k=1
            if i ==24:
                if j >116:
                    k=1
            if i ==26:
                if j >27:
                    k=1
            if i ==27:
                if j >89:
                    k=1
            if i ==28:
                if j >89:
                    k=1
            if i ==29:
                if j >221:
                    k=1
            number=str(i)+"_"+str(j)
            #print(num)
            if number not in odic:
                print(number)
                break
            else:
                tar = odic[number]
            des=tar[0]
            gy=tar[1]
            ji=tar[2]
            des=des.split(",")
            des.pop(0)
            gy=gy.split(",")
            gy.pop(0)
            ji=ji.split(",")
            ji.pop(0)
            des.extend(gy)
            des.extend(ji)
            if k==0:
                for de in des:
                    if de in fdic:
                        num=fdic[de]
                        if num not in vecdic:
                            vecdic[num]=1
                        else:
                            vecdic[num]+=1
                vecdic=sorted(vecdic.items())
                kekka.append(vecdic)
            if k==1:
                for de in des:
                    if de in fdic:
                        num=fdic[de]
                        if num not in vecdic2:
                            vecdic2[num]=1
                        else:
                            vecdic2[num]+=1
                vecdic2=sorted(vecdic2.items())
                kekka2.append(vecdic2)
    return (kekka,kekka2)

pool = mp.Pool(29)
callback = pool.starmap(cul,[(1,2,oridic,feadic),(2,3,oridic,feadic),(3,4,oridic,feadic),(4,5,oridic,feadic),(5,6,oridic,feadic),(6,7,oridic,feadic),(7,8,oridic,feadic),(8,9,oridic,feadic),(9,10,oridic,feadic),(10,11,oridic,feadic),(11,12,oridic,feadic),(12,13,oridic,feadic),(13,14,oridic,feadic),(14,15,oridic,feadic),(15,16,oridic,feadic),(16,17,oridic,feadic),(17,18,oridic,feadic),(18,19,oridic,feadic),(19,20,oridic,feadic),(20,21,oridic,feadic),(21,22,oridic,feadic),(22,23,oridic,feadic),(23,24,oridic,feadic),(24,25,oridic,feadic),(26,27,oridic,feadic),(27,28,oridic,feadic),(28,29,oridic,feadic),(29,30,oridic,feadic)])
l=1
for i in callback:
    if l==25:
        l=26
    for k in i[0]:
        with open("testvec"+str(l)+".txt", "a") as f:
            f.write(str(l)+" ")
        for p in k:
            with open("testvec"+str(l)+".txt", "a") as f:
                f.write(str(p[0])+":"+str(p[1])+" ")
        with open("testvec"+str(l)+".txt", "a") as f:
            f.write("\n")
    for k in i[1]:
        with open("travec.txt", "a") as f:
            f.write(str(l)+" ")
        for p in k:
            with open("travec.txt", "a") as f:
                f.write(str(p[0])+":"+str(p[1])+" ")
        with open("travec.txt", "a") as f:
            f.write("\n")
    l+=1