S = int(input())
y = int(input())
x = int(input())/100
Pl = (S * x / 12) / (1 - ( 1 + x / 12) ** (1 - y * 12))
print(Pl)
print(Pl * y * 12 - S)
