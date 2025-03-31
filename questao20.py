X, Y = map(int, input().split()) 

In, F = (X, Y) if X < Y else (Y, X)

Soma = 0

for i in range(In, F + 1):
    if i % 13 != 0:
        Soma += i

print(Soma) 
