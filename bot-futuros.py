# Bot trading Futuros Binance
import config as cfg
from binance.cm_futures import CMFutures
from datetime import datetime

################################################################## Variables
t = 'BTCUSD_PERP' # Definicion del ticker a comerciar
tf = '1m' # Definicion del periodo de timpo a comerciar

cliente = CMFutures(key=cfg.API_KEY, secret=cfg.API_SECRET)

precio = cliente.ticker_price()


#for i in precio:
#    print(i)



#velas = cliente.klines(t, tf)
#print(velas)
#
#for i in velas:
#    inicio = datetime.fromtimestamp(i[0]/1000)
#    cierre = datetime.fromtimestamp(i[6]/1000)
#    print(f'''
#            Volumen: {i[5]}
#            Inicio: {inicio}
#            Cierre: {cierre}
#    ''')



prof = cliente.depth(t, **{"limit": 1000})

pcompra1 = 0
pcompra2 = 0
pcompra3 = 0
compra1 = []
compra2 = []
compra3 = []

# Precio de compra (3 Bloques mas importantes)
for i in prof['bids']:
    if float(i[1]) > pcompra1:
        pcompra1 = float(i[1])
        compra1 = i
    elif float(i[1]) > pcompra2:
        pcompra2 = float(i[1])
        compra2 = i
    elif float(i[1]) > pcompra3:
        pcompra3 = float(i[1])
        compra3 = i

print(f'''
      Precio de compra 1: {compra1[0]}            Cantidad de compra 1: {compra1[1]}
      Precio de compra 2: {compra2[0]}            Cantidad de compra 2: {compra2[1]}
      Precio de compra 3: {compra3[0]}            Cantidad de compra 3: {compra3[1]}
''')



pventa1 = 0
pventa2 = 0
pventa3 = 0
venta1 = []
venta2 = []
venta3 = []

# Precio de compra (3 Bloques mas importantes)
for i in prof['asks']:
    if float(i[1]) > pventa1:
        pventa1 = float(i[1])
        venta1 = i
    elif float(i[1]) > pventa2:
        pventa2 = float(i[1])
        venta2 = i
    elif float(i[1]) > pventa3:
        pventa3 = float(i[1])
        venta3 = i

print(f'''
      Precio de venta 1: {venta1[0]}            Cantidad de venta 1: {venta1[1]}
      Precio de venta 2: {venta2[0]}            Cantidad de venta 2: {venta2[1]}
      Precio de venta 3: {venta3[0]}            Cantidad de venta 3: {venta3[1]}
''')





def comprar():
    pass



def vender():
    pass
