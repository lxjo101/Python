k = int(input("Wie viele Fibonacci Zahlen sollen berechnet werden: "))

if k == 0:
    print("Keine Fibonacci Zahlen berechnenbar")

if k >= 1:
    zahl1 = 1
    print(zahl1)

if k >= 2:
    zahl2 = 1
    print(zahl2)

for i in range(3, k+1):
    zahl3 = zahl1 + zahl2
    print(zahl3)
    zahl1 = zahl2
    zahl2 = zahl3