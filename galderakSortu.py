import random
import json
import geopy.distance

def distantzia(koord1, koord2):
	emaitza = geopy.distance.distance(koord1, koord2).km #Geopy erabiliz, koordenatuen arteko distantzia kalkulatu KMtan
	return int(round(float(emaitza),0)) #Biribildu eta hamartarrak kendu

def biHerriLortu(datuak):
	with open(datuak) as f:
	    herriakJSON = json.load(f) #JSON fitxategia ireki

	#Ausazko bi zenbaki desberdin lortuko dira, datuetan dagoen herri kopuruaren arabera
	Zherri1 = random.randint(0,len(herriakJSON)-1)
	Zherri2 = random.randint(0,len(herriakJSON)-1)
	while Zherri2 == Zherri1:
		Zherri2 = random.randint(0,len(herriakJSON))

	#Bi herriak lortu
	herri1 = herriakJSON[Zherri1]
	herri2 = herriakJSON[Zherri2]

	izena1 = herri1["itemLabel"] #Herriaren izena lortu
	koord1 = herri1["koord"][6:-1].split(" ") #Herriaren koordenatuak bi elementuko bektore batean sartu
	koord1[0] = float(koord1[0]) #String-etik Float datu motara bihurtu zenbakiak
	koord1[1] = float(koord1[1])

	izena2 = herri2["itemLabel"]
	koord2 = herri2["koord"][6:-1].split(" ")
	koord2[0] = float(koord2[0])
	koord2[1] = float(koord2[1])

	dist = distantzia(koord1, koord2) #Distantzia kalkulatzeko funtzioari deitu

	return izena1, izena2, dist #Lortutako datuak (bi herrien izenak eta distantzia) itzuli

def okerrak(zuzena):
	tartea = int(zuzena*0.5) #Zenbaki tartea lortzeko zenbaki bat definitu, erantzunaren erdia gure kasuan.
	ok1 = random.randint(zuzena-tartea,zuzena+tartea) #Zenbaki tarte horretako ausazko zenbakia lortu
	ok2 = random.randint(zuzena-tartea,zuzena+tartea)

	#Ziurtatu hiru zenbaki horiek ez direla berdinak
	while ok1 == zuzena:
		ok1 = random.randint(zuzena-tartea,zuzena+tartea)

	while (ok2 == zuzena | ok2 == ok1):
		ok2 = random.randint(zuzena-tartea,zuzena+tartea)

	return ok1, ok2

def galderakSortu(datuak, emaitza):
	herriakCSV = open(emaitza, 'w') #CSV fitxategia idazteko moduan ireki
	herriakCSV.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % ('Mota','Galdera','Irudia','Zuzena','Oker1','Oker2','Jatorria','Esteka','Egilea','\n')) #CSV fitxategiko goiburuak idatzi

	for _ in range(100): #100 aldiz
		izena1, izena2, dist = biHerriLortu(datuak) #Datuetatik bi herri eta haien arteko distantzia lortu.
		ok1, ok2 = okerrak(dist) #Erantzun okerrak kalkulatu erantzun zuzenaren arabera
		herriakCSV.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % ('Distantziak', 'Zein da '+izena1+' eta '+izena2+' herrien arteko distantzia zuzena?','',dist+"km",ok1+"km",ok2+"km",'','','Josu Loidi / Alex de Miguel','\n')) #CSV fitxategian galdera sortu

	herriakCSV.close()

#Hasteko funtzioari deia. Datuak gordeta dauden JSON fitxategiaren izena 
#eta galderak gordeko diren CSV fitxategiaren izena hartuko dira parametrotzat
galderakSortu('kontsulta_datuak.json', 'galderak.csv')