import paho.mqtt.client as mqtt
import requests

# Konfiguration für den MQTT-Broker und das Topic
mqtt_broker_address = "mqtt.eclipse.org"  # Beispieladresse, bitte anpassen
mqtt_topic = "dein/topic"

# Callback-Funktion bei Erhalt einer Nachricht vom MQTT-Broker
def on_message(client, userdata, msg):
    try:
        # Extrahiere die Nachricht und führe die Anfrage aus
        request_data = msg.payload.decode("utf-8")
        response_data = make_request(request_data)

        # Sende die Antwort zurück an das MQTT-Topic
        client.publish(mqtt_topic + "/response", response_data)
    except Exception as e:
        print("Fehler beim Verarbeiten der Nachricht:", str(e))

# Funktion zum Weiterleiten der Anfrage an den Server
def make_request(request_data):
    # Hier könnte deine Logik stehen, um die Anfrage zu verarbeiten
    # und eine entsprechende Antwort zu generieren
    # Beispiel: Verwendung der OpenAI API
    openai_url = "https://api.openai.com/v1/engines/davinci/completions"
    openai_api_key = os.getenv("OPENAI_API_KEY") #"DEIN_OPENAI_API_KEY"
    headers = {"Authorization": f"Bearer {openai_api_key}"}
    payload = {"prompt": request_data, "max_tokens": 50}
    response = requests.post(openai_url, headers=headers, json=payload)
    return response.json()["choices"][0]["text"]

# Initialisiere den MQTT-Client
client = mqtt.Client()
client.on_message = on_message

# Verbinde dich mit dem MQTT-Broker
client.connect(mqtt_broker_address, 1883, 60)

# Subscripe zum gewünschten Topic
client.subscribe(mqtt_topic)

# Starte die MQTT-Schleife, um auf Nachrichten zu warten
client.loop_start()

# Halte das Programm am Laufen
try:
    while True:
        pass
except KeyboardInterrupt:
    # Beende die MQTT-Schleife beim Abbruch des Programms
    client.loop_stop()
