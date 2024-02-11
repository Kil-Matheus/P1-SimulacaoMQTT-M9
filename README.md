# P1-SimulacaoMQTT-M9
O código consiste em duas partes: um script de publicação e um script de assinatura MQTT, utilizando a biblioteca paho.mqtt.client. Vale ressaltar que os valores do sensor SPS30 são simulados,baseados em um dataset real, não tendo nenhuma autênticidade nos dados, apenas para fins de estudos.

## Funcionamento
Primeiramente, o broker MQTT precisa ser inicializado e estar em execução para receber e publicar mensagens. Em seguida, os clientes se conectam ao broker para enviar e receber mensagens.

## Script de Publicação MQTT

### Descrição
O script de publicação envia leituras simuladas de um sensor para um tópico MQTT específico.

``` python
[...]
# Loop para publicar mensagens continuamente
try:
    while True:
        # Formatação da mensagem a ser publicada
        message = f'Leitura do sensor:  PM2.5 {zl_1:.2f} (µg/m³), PM10 {zl_2:.2f} (µg/m³), Penha - Zona Leste - SP'
        client.publish("test/topic", message)  # Publica a mensagem no tópico "test/topic"
        print(f"Publicado: {message}")  # Exibe a mensagem publicada
        time.sleep(2)  # Aguarda 2 segundos antes de enviar a próxima leitura
except KeyboardInterrupt:
    print("Publicação encerrada")  # Encerra a publicação em caso de interrupção do teclado

client.disconnect()  # Desconecta do broker MQTT ao final da execução
```

## Script de Assinatura MQTT

### Descrição
O script de assinatura se conecta ao broker MQTT e subscreve a um tópico específico para receber mensagens.

``` python
import paho.mqtt.client as mqtt

# Callback quando uma mensagem é recebida do servidor.
def on_message(client, userdata, message):
    print(f"Recebido: {message.payload.decode()} no tópico {message.topic}")

# Callback para quando o cliente recebe uma resposta CONNACK do servidor.
def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado "+str(rc))
    # Inscreva no tópico aqui, ou se perder a conexão e se reconectar, então as
    # subscrições serão renovadas.
    client.subscribe("test/topic")

# Configuração do cliente
client = mqtt.Client("python_subscriber")
client.on_connect = on_connect
client.on_message = on_message

# Conecte ao broker
client.connect("localhost", 1891, 60)

# Loop para manter o cliente executando e escutando por mensagens
client.loop_forever()
```

Esse é um exemplo simples de comunicação MQTT, onde um cliente publica mensagens em um tópico específico e outro cliente se inscreve nesse tópico para receber e exibir as mensagens recebidas.

## Referências
Links:

https://rmnicola.github.io/m9-ec-encontros/e1

Dataset baseado:

https://static6.arrow.com/aropdfconversion/ce4bd9f646fcec51f56b72f67f1386d6f0b1e95/sensirion_pm_sensors_sps30_datasheet.pdf

## Funcionamento:
Link:

https://drive.google.com/file/d/1bydvb573pQ1tysqiqE7btC7AphYYLCGl/view?usp=sharing