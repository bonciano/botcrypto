## Intento de bot de trading
import os
import config as cfg
from binance.spot import Spot
from datetime import datetime

client = Spot()

# Obtener la hora del servidor
print(client.time())

os.system('echo -----------------------------------------')

# Obtener velas de 1 minuto con un limite de 10
velas = client.klines("BTCUSDT", "1m", limit=10)

# Formato de velas:
#[
#  [
#    1499040000000,      // Open time
#    "0.01634790",       // Open
#    "0.80000000",       // High
#    "0.01575800",       // Low
#    "0.01577100",       // Close
#    "148976.11427815",  // Volume
#    1499644799999,      // Close time
#    "2434.19055334",    // Quote asset volume
#    308,                // Number of trades
#    "1756.87402397",    // Taker buy base asset volume
#    "28.46694368",      // Taker buy quote asset volume
#    "17928899.62484339" // Ignore.
#  ]
#]

os.system('echo -----------------------------------------')

for i in velas:
    inicio = datetime.fromtimestamp(i[0]/1000)
    cierre = datetime.fromtimestamp(i[6]/1000)
    print(f'''
        Volumen: {i[5]}
        Inicio: {inicio}
        Cierre: {cierre}
        ''')


def analisisVelas():
    '''
    Funcion de analisis de velas del Ticker seleccionado
    return 0 --> No realizar accion
    return 1 --> Comprar
    return 2 --> Vender
    '''
    pass












# Creacion de la instancia
client = Spot(key=cfg.API_KEY, secret=cfg.API_SECRET)

# Get account and balance information
#print(client.book_ticker())

# Post a new order
#params = {
#    'symbol': 'BTCUSDT',
#    'side': 'SELL',
#    'type': 'LIMIT',
#    'timeInForce': 'GTC',
#    'quantity': 0.002,
#    'price': 9500
#}
#
## response = client.new_order(**params)
#print(params)
