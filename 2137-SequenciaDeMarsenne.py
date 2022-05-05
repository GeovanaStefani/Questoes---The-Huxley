while True:
    print()
    m = int(input())
    if m<0:
        break

    for i in range(m):
        cont1 = 0
        cont2 = 0
        for c in range(1, i+1):
            if i%c==0:
                cont1+=1
        
        if cont1==2:
            mn = (2**i)-1
            for j in range(1, mn+1):
                if mn%j==0:
                    cont2+=1
        
        if i == 1 or cont2 == 2:
            print("{} ".format(i), end="")