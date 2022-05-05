qntd_desejos = int(input())

desejos = []
realizados = []
faltam = []

for i in range(qntd_desejos):
    desejos.append(input())

qntd_realizados_ditas_por_phoebe = int(input())

for c in range (qntd_realizados_ditas_por_phoebe):
    realizado = input()
    if realizado in desejos:
        realizados.append(realizado)
        qntd_realmente_realizada = qntd_realizados_ditas_por_phoebe 
    else:
        qntd_realmente_realizada = qntd_realizados_ditas_por_phoebe - 1

qntd_faltam = qntd_desejos - qntd_realmente_realizada
for objetivo in desejos:
    if objetivo not in realizados:
        faltam.append(objetivo)

if qntd_faltam == 0:
    print("Smelly Cat, Smelly Cat, what are they feeding you?")
else:
    print("Ainda falta(m) {} objetivo(s)!".format(qntd_faltam))
    for n�o_cumprida in faltam:
        print(n�o_cumprida)