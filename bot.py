## Bot Trading SPOT Binance
# Los pasos a seguir del bot son los siguientes:
# 1) Establecer bloques de ordenes de compra y venta
# 2) Si uno de los bloques se encuentra cercano a la ema de 200, colocar una orden alli.
# 3)  
#
#


################################################################## Librerias
import os
import config as cfg
from binance.spot import Spot
from datetime import datetime
import pandas as pd

################################################################## Variables
t = 'BTCUSDT' # Definicion del ticker a comerciar
tf = '1m' # Definicion del periodo de timpo a comerciar

cliente = Spot()
velas = cliente.klines(t, tf, limit=20)

##################################################################################################################################################### -- Inicio borrar

df = pd.DataFrame(velas)

df[0] = df[0].datetime.fromtimestamp() / 1000 
df[4] = df.iloc[:,1].rolling(window=3).mean()
print(df)

#for i in velas:
#    inicio = datetime.fromtimestamp(i[0]/1000)
#    cierre = datetime.fromtimestamp(i[6]/1000)
#    print(f'''
#            Volumen: {i[5]}
#            Inicio: {inicio}
#            Cierre: {cierre}
#    ''')
#
#
#
#def compra(precio):
#    '''
#    Funcion de compra
#    '''
#    pass
#
#
#def venta(precio):
#    '''
#    Funcion de venta
#    '''
#    pass
#
#
#
#
#
#prof = cliente.depth(t,limit=5000)
#
#pcompra1 = 0
#pcompra2 = 0
#pcompra3 = 0
#compra1 = []
#compra2 = []
#compra3 = []
#
## Precio de compra (3 Bloques mas importantes)
#for i in prof['bids']:
#    if float(i[1]) > pcompra1:
#        pcompra1 = float(i[1])
#        compra1 = i
#    elif float(i[1]) > pcompra2:
#        pcompra2 = float(i[1])
#        compra2 = i
#    elif float(i[1]) > pcompra3:
#        pcompra3 = float(i[1])
#        compra3 = i
#
#print(f'''
#      Precio de compra 1: {compra1[0]}            Cantidad de compra 1: {compra1[1]}
#      Precio de compra 2: {compra2[0]}            Cantidad de compra 2: {compra2[1]}
#      Precio de compra 3: {compra3[0]}            Cantidad de compra 3: {compra3[1]}
#''')
#
#
#
#pventa1 = 0
#pventa2 = 0
#pventa3 = 0
#venta1 = []
#venta2 = []
#venta3 = []
#
## Precio de compra (3 Bloques mas importantes)
#for i in prof['asks']:
#    if float(i[1]) > pventa1:
#        pventa1 = float(i[1])
#        venta1 = i
#    elif float(i[1]) > pventa2:
#        pventa2 = float(i[1])
#        venta2 = i
#    elif float(i[1]) > pventa3:
#        pventa3 = float(i[1])
#        venta3 = i
#
#print(f'''
#      Precio de venta 1: {venta1[0]}            Cantidad de venta 1: {venta1[1]}
#      Precio de venta 2: {venta2[0]}            Cantidad de venta 2: {venta2[1]}
#      Precio de venta 3: {venta3[0]}            Cantidad de venta 3: {venta3[1]}
#''')
#
#
#
#
#
#
#
#
#
########################
######################## Recordatorio
######################## Cuando ingrese a una operacion, colocar stop loss, stop profit y take profit.
########################
########################
########################
########################
########################
########################
#
#
#
#
#
#
#
#
#
#
#
#
#
#'''
#print('Precio de venta --------------------------------------')
## Precio de venta
#for i in prof['asks']:
#    print(f'Precio: {i[0]}      Cantidad: {i[1]}')
#'''
#
#
###################################################################################################################################################### -- Fin borrar
#
#
#os.system('echo ----------------Inico de analisis-------------------------')
#
#
##def importarTicker(t):
##    '''
##    Funcion para importar datos del Ticker definido de un periodo de tiempo determinado
##    '''
##    cliente = Spot()
##    t = 'BTCUSDT' # Definicion del ticker a comerciar
##    tf = '1m' # Definicion del periodo de timpo a comerciar
##    velas = cliente.klines(t, tf, limit=8)
##
##    for i in velas:
##        inicio = datetime.fromtimestamp(i[0]/1000)
##        cierre = datetime.fromtimestamp(i[6]/1000)
##        print(f'''
##            Volumen: {i[5]}
##            Inicio: {inicio}
##            Cierre: {cierre}
##            ''')
##
#
#
#
#
#def analisisMediaMovil():
#    '''
#    Funcion de analisis de soporte segun el Ticker seleccionado
#    return 0 --> No realizar accion
#    return 1 --> Comprar
#    return 2 --> Vender
#    '''
#    pass
#
#
#def analisisSoporte():
#    '''
#    Funcion de analisis de soporte segun el Ticker seleccionado
#    return 0 --> No realizar accion
#    return 1 --> Comprar
#    return 2 --> Vender
#    '''
#    pass
#
#def analisisResistencia():
#    '''
#    Funcion de analisis de resistencia segun el Ticker seleccionado
#    return 0 --> No realizar accion
#    return 1 --> Comprar
#    return 2 --> Vender
#    '''
#    pass
#
#
#def analisisTendencia():
#    '''
#    Funcion de analisis de tendencia segun el Ticker seleccionado
#    return 0 --> No realizar accion
#    return 1 --> Comprar
#    return 2 --> Vender
#    '''
#    pass
#
#def analisisVolumen():
#    '''
#    Funcion de analisis de volumen segun el Ticker seleccionado
#    return 0 --> No realizar accion
#    return 1 --> Comprar
#    retirn 2 --> Vender
#    '''
#    pass
#
#def analisisVelas():
#    '''
#    Funcion de analisis de velas del Ticker seleccionado
#    return 0 --> No realizar accion
#    return 1 --> Comprar
#    return 2 --> Vender
#    '''
#    pass
#
## Creacion de la instancia
#client = Spot(key=cfg.API_KEY, secret=cfg.API_SECRET)
#
## Get account and balance information
##print(client.book_ticker())
#
## Post a new order
##params = {
##    'symbol': 'BTCUSDT',
##    'side': 'SELL',
##    'type': 'LIMIT',
##    'timeInForce': 'GTC',
##    'quantity': 0.002,
##    'price': 9500
##}
##
### response = client.new_order(**params)
##print(params)
#
#
#
#
## Formato de velas:
##[
##  [
##    1499040000000,      // Open time
##    "0.01634790",       // Open
##    "0.80000000",       // High
##    "0.01575800",       // Low
##    "0.01577100",       // Close
##    "148976.11427815",  // Volume
##    1499644799999,      // Close time
##    "2434.19055334",    // Quote asset volume
##    308,                // Number of trades
##    "1756.87402397",    // Taker buy base asset volume
##    "28.46694368",      // Taker buy quote asset volume
##    "17928899.62484339" // Ignore.
##  ]
##]


