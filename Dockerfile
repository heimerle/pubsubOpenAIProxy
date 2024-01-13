# Verwende das offizielle Python-Image als Basis
FROM python:3.8

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Installiere die notwendigen Python-Pakete und MQTT-Bibliothek
RUN pip install paho-mqtt requests

# Kopiere die lokalen Dateien in das Arbeitsverzeichnis des Containers
COPY . /app

# Definiere Umgebungsvariablen (ersetze mit deinen eigenen Werten)
ENV MQTT_BROKER_ADDRESS "mqtt.eclipse.org"
ENV MQTT_TOPIC "dein/topic"
ENV OPENAI_API_KEY "DEIN_OPENAI_API_KEY"

# Starte den Proxy beim Start des Containers
CMD ["python", "proxy_script.py"]
