def CalculaMaior(a, b):
    
    maior = (a+b+ abs(a-b))/2
    
    return int(maior)

a, b, c = map(int, input().split())

print("{} eh o maior".format(CalculaMaior(CalculaMaior(a, b), c)))