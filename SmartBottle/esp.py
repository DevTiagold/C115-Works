import time
import json
import random
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"  # ou "localhost" se rodar Mosquitto local
PORT = 1883
TOPIC_TEMP = "perseverai/garrafa1/temperatura"
TOPIC_NIVEL = "perseverai/garrafa1/nivel"
TOPIC_CMD   = "perseverai/garrafa1/comando"

nivel_atual = 0      # ml consumidos no dia
meta_diaria = 2000   # 2000 ml

def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker com código:", rc)
    # assina comandos vindos do app
    client.subscribe(TOPIC_CMD)

def on_message(client, userdata, msg):
    global nivel_atual
    print("Mensagem recebida:", msg.topic, msg.payload.decode())
    try:
        data = json.loads(msg.payload.decode())
        if data.get("comando") == "reset_meta":
            nivel_atual = 0
            print("Meta diária resetada pelo aplicativo.")
    except Exception as e:
        print("Erro ao processar comando:", e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        # simula temperatura entre 25 e 45 ºC
        temperatura = round(random.uniform(25, 45), 1)

        # simula consumo de 50 a 150 ml por "ciclo"
        consumo = random.randint(50, 150)
        nivel_atual += consumo
        if nivel_atual > meta_diaria:
            nivel_atual = meta_diaria

        # nível em %
        nivel_percent = int((nivel_atual / meta_diaria) * 100)

        # monta os JSON
        payload_temp = json.dumps({
            "device_id": "garrafa1",
            "temperatura": temperatura
        })

        payload_nivel = json.dumps({
            "device_id": "garrafa1",
            "nivel_percent": nivel_percent,
            "consumo_ml": nivel_atual
        })

        # publica
        client.publish(TOPIC_TEMP, payload_temp)
        client.publish(TOPIC_NIVEL, payload_nivel)

        print("Enviado:",
              "\n  Temperatura:", temperatura,
              "\n  Nível:", nivel_percent, "% (", nivel_atual, "ml )")

        time.sleep(5)  # a cada 5 segundos

except KeyboardInterrupt:
    print("Simulação encerrada.")
    client.loop_stop()
    client.disconnect()
