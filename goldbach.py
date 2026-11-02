# Laborator 4 - Cerinta 1: Conjectura lui Goldbach
# Student: Garneata Dragos

def este_prim(n):
    # un numar mai mic sau egal cu 1 nu este prim
    if n <= 1:
        return False
    if n == 2:
        return True
    # daca e par si diferit de 2, nu e prim
    if n % 2 == 0:
        return False
    # verificam divizorii impari pana la radical din n
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def gaseste_perechi_goldbach(n):
    # gasim perechile (p, q) cu p <= q si p + q = n
    perechi = []
    for p in range(2, n // 2 + 1):
        q = n - p
        if este_prim(p) and este_prim(q):
            perechi.append((p, q))
    return perechi

def citeste_numar_par():
    while True:
        valoare = input("Introduceti un numar natural par mai mare decat 2: ").strip()
        try:
            n = int(valoare)
        except ValueError:
            print("Eroare: Valoarea introdusa nu este un numar intreg valid!\n")
            continue
        
        if n <= 2:
            print("Eroare: Numarul trebuie sa fie strict mai mare decat 2 (n > 2)!\n")
            continue
        
        if n % 2 != 0:
            print("Eroare: Numarul introdus nu este par!\n")
            continue
        
        return n

def main():
    print("=== Conjectura lui Goldbach ===")
    n = citeste_numar_par()
    
    perechi = gaseste_perechi_goldbach(n)
    
    if perechi:
        print(f"\nDescompunerile lui {n} in suma de doua numere prime (p <= q):")
        for p, q in perechi:
            print(f"{n} = {p} + {q}")
    else:
        print(f"\nNu s-a gasit nicio descompunere pentru {n}.")

if __name__ == "__main__":
    main()
