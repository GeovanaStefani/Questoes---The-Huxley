QNTD_NUMS = 3

def volumeEsfera(raio):
    pi = 3.1416
    volume = (4*pi*(raio**3))/3
    return volume
        
for i in range(QNTD_NUMS):
    raio = float(input())
    print("{:.2f}".format(volumeEsfera(raio)))