tab = list(map(int, input("Podaj liczby oddzielone spacja: ").split()))
n = len(tab)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if tab[j] > tab[j + 1]:
            tab[j], tab[j + 1] = tab[j + 1], tab[j]
        print("i =", i, "j =", j, tab)

print("Wynik:", tab)
