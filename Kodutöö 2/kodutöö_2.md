Luua lihtne rollimängu tegelaste süsteem, mis demonstreerib nelja objorienteeritud proge põhimõtet
                  (abstraktsioon, pärilus, polümorfism, kapseldamine)

Vajalik:

Main klass Tegelane, alamklassid - Sõdalane, Maag, Vibukütt, fuktsioon lahing (t1,t2)
Main klass peab olema abstraktne (ABC)
Meetod ründa() peab olema abstraktne, kõik tegelased kasutavad seda

Alamklassid peavad pärima main klassist - nime, elupunktid, meetod võta kahju (), meetod on elus (),
Fn lahing() ei tohi kontrollida tüüpe:
- keelatud if isinstance(t1, Maag)
- lubatud t1.ründa(t2)
- funktsioon peab töötama iga tegelasega

Elupunktid peavad olema _elu
Maagil peab olema _mana
Vibukütil peab olema _nooled
(midagi ei tohi negatiivseks muutuda), kõik muutused peavad toimuma meetodite kaudu

1. Võimaldab kahe tegelase lahingut ( tegelased ründavad kordamööda kuni elud 0)
2. Igal tegelasel peab olema erinev ründeloogika ( Sõdalane - juhuslik kahju 10-20), 
    (Maag - kasutab mana ja mana väheneb), (Vibukütt - kasutab nooli ja nooled vähenevad)
3. Midagi ei tohi alla 0 minna
4. Programm peab töötama ilma vigadeta
5. Lisada kommentaar - mida peaks muutma, kui lisada uus tegelane
6. Tähtaeg 13.märts


Uue tegelase lisamiseks:
- pärimine Tegelane klassist, kasuta abstraktset meetodit ründa(),
- Lisa vajalikud eriväljad nagu mana või nooled,
- Lahing funktsioon töötab automaatselt.
