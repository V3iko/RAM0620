from abc import ABC, abstractmethod
import random
from fcntl import FASYNC


class Tegelane(ABC):
    def __init__(self, nimi: str, elupunktid: int):
        self.nimi = nimi
        self._elupunktid = elupunktid # Kapseldamine ehk elupunktid on privaatne, peab endale selgeks tegema

    @abstractmethod
    def ründa(self, vastane): # Abstraktsioon
        pass

    def võtab_kahju(self, kahju):
        self._elupunktid = max(0, self._elupunktid - kahju) # Elud ei lähe alla 0

    def on_elus(self):
        return self._elupunktid > 0

    def näita_elusid(self):
        return self._elupunktid

class Sõdalane(Tegelane): # Pärib main klassist nime ja elupunktid
    def ründa(self, vastane): # Abstraktsioon
        kahju = random.randint(10, 20)
        print(f"{self.nimi} lööb mõõgaga, tegi {kahju} DMG!")
        vastane.võtab_kahju(kahju)

class Maag(Tegelane):
    def __init__(self, nimi: str, elupunktid: int, mana: int): # Pärib main klassist nime ja elupunktid
        super().__init__(nimi, elupunktid)
        self._mana = mana # Kapseldamine
        self._külmunud = False # Külmutamis effekt

    def ründa(self, vastane): # Abstraktsioon
        if self._mana < 5:
            print(f"{self.nimi} ei saa rünnata, mana puudub!")
            return

        kahju = random.randint(10, 20)
        self._mana -= 5
        print(f"{self.nimi} viskab loitsu, tegi {kahju} DMG, mana alles: {self._mana}")
        vastane.võtab_kahju(kahju)

        # Juhuslik külmutus 30% tõenäosusega
        if random.random() < 0.3:
            vastane._külmunud = True
            print(f"{vastane.nimi} on külmunud ja kaotab järgmisel ringil rünnaku!")

class Vibukütt(Tegelane):
    def __init__(self, nimi: str, elupunktid: int, nooled: int): # Pärib main klassist nime ja elupunktid
        super().__init__(nimi, elupunktid)
        self._nooled = nooled # Kapseldamine

    def ründa(self, vastane): # Abstraktsioon
        if self._nooled <= 0:
            print(f"{self.nimi} ei saa vibu vinnastada, nooled puuduvad!")
            return

        if random.random() < 0.5:
            kahju = random.randint(10, 20)
            tüüp = ("eriti terava noole")

        else:
            kahju = random.randint(5, 10)
            tüüp = ("tavalise noole")

        self._nooled -= 1
        print(f"{self.nimi} tulistab {tüüp}, tegi {kahju} DMG, nooli alles: {self._nooled}")
        vastane.võtab_kahju(kahju)

def lahing(t1, t2): # Polümorfism

    print(f"Lahing algab: {t1.nimi} vs {t2.nimi}\n")
    t1._külmunud = False
    t2._külmunud = False

    while t1.on_elus() and t2.on_elus():
        if getattr(t1, "_külmunud", False):
            print(f"{t1.nimi} on külmunud ja kaotab rünnaku!")
            t1._külmunud = False

        else:
           t1.ründa(t2)

        if not t2.on_elus():
            print(f"{t2.nimi} on surnud!")
            break

        if getattr(t2, "_külmunud", False):
            print(f"{t2.nimi} on külmunud ja kaotab rünnaku!")
            t2._külmunud = False

        else:
           t2.ründa(t1)

        if not t1.on_elus():
            print(f"{t1.nimi} on surnud!")
            break
        print(f"{t1.nimi} elud: {t1.näita_elusid()}, {t2.nimi} elud: {t2.näita_elusid()}\n")

def main():

    s = Sõdalane("Arthur", 100)
    m = Maag("Merlin", 75, 25)
    v = Vibukütt("Jacob", 80, 10)

    lahing(v, m)

if __name__ == "__main__":
    main()

