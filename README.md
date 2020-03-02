# EguneanBehin: distantzia zuzenak
Egunean Behin aplikazioak aurkeztu duen lehiaketan parte hartzeko gure proposamena. Programa txiki honekin Euskal Herriko herrien arteko distantzi zuzenen inguruko galderak sortu litezke.


Horretarako, WikiData hartu da oinarritzat. Bertan, kontsulta bat eginez (https://w.wiki/JXe) Euskal Herriko herri guztiak lortu dira, hauen koordenatuekin batera. Datu hauek JSON fitxategi batean gordeta deskargatu dira, zuzenean informazio guztia lokalean izateko.

#### Programaren funtzionamendua
Proiektu osoa hiru fitxategiz osatuta dago:
* **galderakSortu.py**: programa bera Python programazio lengoaian idatzita. Hau da exekutatu behar den fitxategia.
* **kontsulta_datuak.json**: WikiDatatik lortu diren datuak biltzen dituen JSON fitxategia.
* **galderak.csv**: irteerako fitxategia. Bertan, programak sortu dituen galderak idatziko dira.
