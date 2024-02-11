import paho.mqtt.client as mqtt
import time
from sensor_SPS30 import simular_leitura_sensor

# Configuração do cliente
client = mqtt.Client("Conexão Zona Leste - SP")

# Conecte ao broker
client.connect("localhost", 1891, 60)

# Loop para publicar mensagens continuamente
try:
    while True:
        #valores
        zl_1, zl_2 = simular_leitura_sensor()
        message = f'Leitura do sensor:  PM2.5 {zl_1:.2f} (µg/m³), PM10 {zl_2:.2f} (µg/m³), Penha - Zona Leste - SP'
        client.publish("test/topic", message)
        print(f"Publicado: {message}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Publicação encerrada")

client.disconnect()