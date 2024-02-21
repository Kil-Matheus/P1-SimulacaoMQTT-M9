import random
import time

def simular_leitura_sensor():
    # Simula uma leitura dO sensor SPS30, existem 2 valores, PM2.5 (µg/m³), PM10 (µg/m³)
    var_1 = random.uniform(0, 10)
    var_2 = random.uniform(10, 20)
    return var_1, var_2
    
# Simular leituras do sensor a cada segundo
# for _ in range(10):
#     valor = simular_leitura_sensor()
#     print(f'Leitura do sensor: {var_1}, {var_2}')
#     time.sleep(1)
