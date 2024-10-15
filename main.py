from Tablica import Tablica

def main():
    a = int(input("Podaj wartość a: "))
    b = int(input("Podaj wartość b: "))

    mojatablica = Tablica(10)
    mojatablica.wypelnij(a, b)
    print("Tablica:", mojatablica.numbers)
    print("Maksymalna wartość:", mojatablica.maksimum())
    print("Minimalna wartość:", mojatablica.minimum())
    print("Druga maksymalna wartość:", mojatablica.maksimum2())
    wyszukaj = int(input("Podaj wartość do wyszukania: "))
    indeks = mojatablica.znajdz(wyszukaj)

    if indeks != -1:
        print(f"Wartość {wyszukaj} znaleziona na indeksie: {indeks+1}")
    else:
        print(f"Wartość {wyszukaj} nie została znaleziona w tablice.")

main()