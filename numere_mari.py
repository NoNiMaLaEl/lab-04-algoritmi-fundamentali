# Laborator 4 - Cerinta 2: Adunarea si inmultirea numerelor mari
# Student: Garneata Dragos

import os

def citeste_numere(cale_fisier=None):
    if cale_fisier is None:
        if os.path.exists("numere.txt"):
            cale_fisier = "numere.txt"
        else:
            cale_script = os.path.dirname(os.path.abspath(__file__))
            cale_fisier = os.path.join(cale_script, "numere.txt")

    # verificam existenta fisierului
    if not os.path.exists(cale_fisier):
        print(f"Eroare: Fisierul '{cale_fisier}' nu exista!")
        return None
    
    try:
        with open(cale_fisier, "r") as f:
            linii = [linie.strip() for linie in f.readlines() if linie.strip()]
    except Exception as e:
        print(f"Eroare la citirea fisierului: {e}")
        return None
    
    if len(linii) < 2:
        print("Eroare: Fisierul trebuie sa contina cel putin doua numere (pe linii separate)!")
        return None
    
    numere = []
    for idx, linie in enumerate(linii[:2], 1):
        if not linie.isdigit():
            print(f"Eroare: Linia {idx} contine caractere invalide (trebuie doar cifre)!")
            return None
        if len(linie) > 200:
            print(f"Eroare: Numarul de pe linia {idx} depaseste limita de 200 de cifre!")
            return None
        # eliminam zerourile nesemnificative de la inceput
        curatat = linie.lstrip("0")
        numere.append(curatat if curatat else "0")
        
    return numere[0], numere[1]

def aduna(a, b):
    # adunare cifra cu cifra de la dreapta la stanga folosind transportul
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    rezultat = []
    
    while i >= 0 or j >= 0 or carry:
        c1 = int(a[i]) if i >= 0 else 0
        c2 = int(b[j]) if j >= 0 else 0
        
        suma = c1 + c2 + carry
        rezultat.append(str(suma % 10))
        carry = suma // 10
        
        i -= 1
        j -= 1
        
    rezultat.reverse()
    s = "".join(rezultat).lstrip("0")
    return s if s else "0"

def inmulteste_cu_cifra(numar, cifra):
    # inmultirea unui numar mare cu o singura cifra
    if cifra == 0:
        return "0"
    carry = 0
    rez = []
    for i in range(len(numar) - 1, -1, -1):
        prod = int(numar[i]) * cifra + carry
        rez.append(str(prod % 10))
        carry = prod // 10
    if carry:
        rez.append(str(carry))
    rez.reverse()
    return "".join(rez)

def inmulteste(a, b):
    # inmultirea prin metoda inmultirii in coloana (produse partiale si transport)
    if a == "0" or b == "0":
        return "0"
    if a == "1":
        return b
    if b == "1":
        return a
        
    total = "0"
    # parcurgem cifrele celui de-al doilea numar de la dreapta la stanga
    for idx, c in enumerate(reversed(b)):
        cifra = int(c)
        produs_partial = inmulteste_cu_cifra(a, cifra)
        if produs_partial != "0":
            # adaugam zerourile corespunzatoare pozitiei
            produs_partial += "0" * idx
        total = aduna(total, produs_partial)
        
    return total

def main():
    print("=== Adunarea si inmultirea numerelor mari ===")
    date = citeste_numere()
    if date is None:
        return
    
    num1, num2 = date
    print(f"Numarul 1: {num1}")
    print(f"Numarul 2: {num2}\n")
    
    suma = aduna(num1, num2)
    produs = inmulteste(num1, num2)
    
    print(f"Suma:     {suma}")
    print(f"Produsul: {produs}")

if __name__ == "__main__":
    main()
