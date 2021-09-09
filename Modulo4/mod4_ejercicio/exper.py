diccPrenda_Tarifa = {'POLO':.50,'CAMISA':1.50,'PANTALON':1.50}
diccCatego_Bonus = {'A':250.00,'B':150.00,'C':100.00,'D':50.00}
# diccPrenda_Tarifa = ('POLO',.50,'CAMISA',1.50,'PANTALON',1.50)
# diccCatego_Bonus = ('A',250.00,'B',150.00,'C',100.00,'D',50.00)
tipoPrenda='POLO'
pagoTarifa=0,0
pagoBoni=0.0
cantPrendas=800
categoriaBoni="C"

# for key in diccPrenda_Tarifa.keys():
#         # val=diccPrenda_Tarifa[key]
#         if diccPrenda_Tarifa[key]==diccPrenda_Tarifa[tipoPrenda]:
#             pagoTarifa=diccPrenda_Tarifa[key]
            # break
# for key in diccCatego_Bonus:
#     if cantPrendas > 700 and key==categoriaBoni:
#         pagoBoni = categoriaBoni[key]
#         break
#     else:
#         pagoBoni=0.0

for i in (diccPrenda_Tarifa,diccCatego_Bonus):
    if prenda==tipoPrenda and categoria==categoriaBoni and cantPrendas>700:
        pagoTarifa=diccPrenda_Tarifa[prenda]
        pagoBoni=diccCatego_Bonus[categoria]
        break
    else:
        pagoBoni=0.0

print(pagoBoni,pagoBoni)
for i in (diccPrenda_Tarifa,diccCatego_Bonus):
    if prenda==tipoPrenda and categoria==categoriaBoni and cantPrendas>700:
        pagoTarifa=diccPrenda_Tarifa[prenda]
        pagoBoni=diccCatego_Bonus[categoria]
        break
    else:
        pagoBoni=0.0