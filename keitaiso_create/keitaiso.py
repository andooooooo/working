import re
import sys
from pyknp import Juman
import multiprocessing as mp

p10 = re.compile('[^一-龥^ぁ-ん^ァ-ン^々^ー^、^。]+')

def remove(text):
    text = re.sub(r'[a-zA-Z0-9¥"¥.¥,¥@]+', '', text)
    text = re.sub(r'[!"“#$%&()\*\+\-\.,\/:;<=>?@\[\\\]^_`{|}~]', '', text)
    text = re.sub(r'[\n|\r|\t]', '', text)
    text = text.replace(" ", '')
    #jp_chartype_tokenizer = nltk.RegexpTokenizer(u'([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+|[ぁ-んァ-ンー\u4e00-\u9FFF]+|[々。、])')
    #text = "".join(jp_chartype_tokenizer.tokenize(text))
    #text=re.split(p10,text)
    #text="".join(text)
    #text=text.encode('utf-8')
    return text

p=0
odic={}
h = open("original.csv")
lines = h.readlines()
for i in lines:
    i=i.split("\t")
    three=i[3].rstrip()
    odic[i[0]]=(i[1],i[2],three)

def cul(sta,en,oridic):
    templist=[]
    for i in range(sta,en):
        for j in range(1,4000):
            zantei=["","",""]
            dwords=""
            gawords=""
            gywords=""
            #try:
            number=str(i)+"_"+str(j)
            if number not in oridic:
                print(number)
                break
            else:
                tar = oridic[number]
            #print(number)
            des=tar[0]
            gaiyou=tar[1]
            gyoumu=tar[2]
            jumanpp = Juman()
            des=remove(des)
            gaiyou=remove(gaiyou)
            gyoumu=remove(gyoumu)
            try:
                p=0
                if not des=="":
                    des=jumanpp.analysis(des)
                    for mrph in des.mrph_list():
                        if mrph.hinsi=="助詞" or mrph.hinsi=="助動詞" or mrph.hinsi=="特殊" or mrph.bunrui=="数詞":
                            continue
                        else:
                            dwords=dwords+","+  mrph.midasi
                zantei[0]=dwords
                p=1
                if not gaiyou=="":
                    gaiyou=jumanpp.analysis(gaiyou)
                    for mrph in gaiyou.mrph_list():
                        if mrph.hinsi=="助詞" or mrph.hinsi=="助動詞" or mrph.hinsi=="特殊" or mrph.bunrui=="数詞":
                            continue
                        else:
                            gawords=gawords+","+ mrph.midasi
                zantei[1]=gawords
                p=2
                if not gyoumu=="":
                    gyoumu=jumanpp.analysis(gyoumu)
                    for mrph in gyoumu.mrph_list():
                        if mrph.hinsi=="助詞" or mrph.hinsi=="助動詞" or mrph.hinsi=="特殊" or mrph.bunrui=="数詞":
                            continue
                        else:
                            gywords=gywords+","+  mrph.midasi
                zantei[2]=gywords
                templist.append(number+" "+zantei[0]+" "+zantei[1]+" "+zantei[2]+"\n")
            except:
                templist.append(number+" "+zantei[0]+" "+zantei[1]+" "+zantei[2]+"\n")
                print(number+"cont"+str(p))
                continue
    return templist
pool = mp.Pool(29)
callback = pool.starmap(cul,[(1,2,odic),(2,3,odic),(3,4,odic),(4,5,odic),(5,6,odic),(6,7,odic),(7,8,odic),(8,9,odic),(9,10,odic),(10,11,odic),(11,12,odic),(12,13,odic),(13,14,odic),(14,15,odic),(15,16,odic),(16,17,odic),(17,18,odic),(18,19,odic),(19,20,odic),(20,21,odic),(21,22,odic),(22,23,odic),(23,24,odic),(24,25,odic),(26,27,odic),(27,28,odic),(28,29,odic),(29,30,odic)])
for i in callback:
    for k in i:
        with open("keitaiso.csv", "a") as f:
            f.write(k)