par = []
impar = []
for i in range(15):
    num = int(input())
    if num%2==0:
        if (len(par)<5):
            par.append(num)
        else:
            for j in range(5):
                print("par[{}] = {}".format(j, par[j]))
            par = []
            par.append(num)
    else:
        if len(impar)<5:
            impar.append(num)
        else:
            for c in range(5):
                print("impar[{}] = {}".format(c, impar[c]))
            impar = []
            impar.append(num)   

if len(impar)!=0:
    for l in range(len(impar)):
        print("impar[{}] = {}".format(l, impar[l]))
if len(par)!=0:
    for k in range(len(par)):
        print("par[{}] = {}".format(k, par[k]))