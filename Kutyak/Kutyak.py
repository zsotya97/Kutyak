from Adatok import *
import datetime as dt


#Metódus az adatok beolvasásához
def Beolvasas(nev,osztaly):
    with open(nev, "r", encoding="utf-8") as Beolvas:
        fejlec = Beolvas.readline()
        return [osztaly(x.strip()) for x in Beolvas]


#Beolvasás feladatok
kutyafajtak = Beolvasas("KutyaFajtak.csv",KutyaFajtak)
kutyanevek = Beolvasas("KutyaNevek.csv", KutyaNevek)
kutyak = Beolvasas("Kutyak.csv", Kutyak)

#3. feladat: listában lévő adatok száma
print(f"3. feladat: Kutyanevek száma: {len(kutyanevek)}")
eletkor =0
maxev=maxid=maxfid=0
#Átlag életkor és az azonosítók kikeresése 7. feladathoz
for x in kutyak:
    eletkor+=x.eletkor
    if x.eletkor>maxev : 
       maxev=x.eletkor
       maxid=x.nev_id
       maxfid=x.fajta_id

#6. feladat
atlag = float(sum(x.eletkor for x in kutyak)/len(kutyak))
print(f"6. feladat: Kutyák átlag életkora: %.2f" %atlag)

#7 feladat:
print("7. feladdat: Legidősebb kutya neve és fajtája:",end=" ")
legidosebb=""
for x in kutyanevek:
    if x.id==maxid: legidosebb+=f"{x.kutya_nev}, "
for x in kutyafajtak:
    if x.id==maxfid: legidosebb+=f"{x.nev}"
print(legidosebb)



#8. feladat:
print("8. feladat: Január 10-én vizsgált kutyák száma: ")
fid= [x.fajta_id for x in kutyak if x.ellenorzes.month ==1 and x.ellenorzes.day==10]
tizedike = {}
for x in fid:
    for y in kutyafajtak:
        if y.id==x: 
            neve=y.nev
            tizedike[neve]=tizedike.get(neve,0)+1
[print(f"\t{neve}: {tiz} kutya") for neve, tiz in tizedike.items()]

#9. feladat
kivalogatas=[]
maxell=0
maxdatum = dt.datetime(1,1,1)
for x in kutyak:
    szam=0
    for y in kivalogatas:
        if y==x.ellenorzes: szam+=1
    if szam==0: kivalogatas.append(x.ellenorzes)
for x in kivalogatas:
    szamolas=0
    for y in kutyak:
        if x==y.ellenorzes:
            szamolas+=1
    if szamolas>maxell:
        maxell=szamolas
        maxdatum=x
print(f"9. feladat: Legjobban leterhelt nap: {dt.datetime.strftime(maxdatum, '%Y. %m. %d')}: {maxell} kutya")

#10. feladat
print("10. feladat: névstatisztika.txt")
statisztika=[]
with open("névstatisztika.csv","w", encoding="utf-8") as kiiras:
    for x in kutyanevek:
        szamlalas=0
        for y in kutyak:
            if x.id==y.nev_id:
                szamlalas+=1
        statisztika.append(Statisztika(x.kutya_nev,szamlalas))
    statisztika=sorted(statisztika, key=lambda x: x.szam, reverse=True)
    [kiiras.write(f"{x.nev}:{x.szam}\n") for x in statisztika]
        

            

        
    