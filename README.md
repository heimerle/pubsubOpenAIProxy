# pubsubOpenAIProxy
Message Broker Proxy to openAI  

the main idea is to use AI capability on my ESP8266 and ESP32 devices, but not directly as they communicate via MQTT with my whole smart Home environment 


docker run -e MQTT_BROKER_ADDRESS="your_broker_address" MQTT_TOPIC = "topic" OPEN_API_KEY="your_openAI_API_key" docker_image_name

