from typing import List, Tuple

ROMAN_NUMERALS: List[Tuple[int, str]] = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]
def teisendus(n: int) -> str:
    """
    Teisendame kontrollitud arvu rooma numbriteks
    """
    osad = []
    for value, symbol in ROMAN_NUMERALS:
        while n >= value:
            n -= value
            osad.append(symbol)
    return "".join(osad)

def sisend(min_nr: int, max_nr: int) -> int:
    """
    Võtame kasutajalt sisendi ja kontrollime seda
    Tagastame kontrollitud arvu
    """
    while True:
        s = input(f"\nSisestage täisarv vahemikus {min_nr}-{max_nr}: ")

        try:
            n = int(s)
        except ValueError:
            print("Sisend peab olema täisarv (nt 35). Proovige uuesti!")
            continue

        if not (min_nr <= n <= max_nr):
            print(f"Sisestatud arv peab olema vahemikus {min_nr}-{max_nr}. Proovige uuesti!")
            continue

        return n

def kas_j2tkata() -> bool:
    """
    Kontrollime kas kasutaja soovib jätkata
    """
    while True:
        vastus = input("\nKas soovite jätkata? (jah/ei): ").strip().lower()
        if vastus in "jah":
            return True
        if vastus in "ei":
            return False
        print("Palun sisestage jah või ei!")

def main():
    """
    - Saame kasutajalt sisendi, kontrollime seda
    - Muudame sisendi rooma numbriteks
    - Hoiame programmi tsüklis kuni kasutaja soovib lõpetada
    """

    print("---TÄISARVU KONVERTER ROOMA NUMBRITEKS---")
    while True:
       arv = sisend(1, 1000)
       print(f"Teie rooma number on: {teisendus(arv)}")

       if not kas_j2tkata():
           print("Head aega!")
           break

if __name__ == "__main__":
    main()