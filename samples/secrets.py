# WiFi Settings
SSID = '<SSID>'
PASSWORD = '<SSID_PASSWORD>'

# IoT Hub Settings
# Use the following values to configure your IoT Hub connection 
IOTHUB_CLIENTID = '<CLIENT_ID>'
IOTHUB_HOSTNAME = '<IOT_HUB_HOSTNAME>'

IOTHUB_USERNAME = '{hostname}/{clientid}/?api-version=2021-04-12'.format(hostname = IOTHUB_HOSTNAME, clientid = IOTHUB_CLIENTID)
IOTHUB_PASSWORD = '<SHARED_ACCESS_SIGNATURE_TOKEN>'
IOTHUB_TOPIC_PUB = b'devices/{clientid}/messages/events/'.format(clientid = IOTHUB_CLIENTID)
#IOTHUB_TOPIC_MSG = b'{"buttonpressed":"1"}'

# IoT Hub using MQTT Port 8883 for secure connection
# Leave IOTHUB_PORT_NO = 0 and the connection will default to 8883
IOTHUB_PORT_NO = 0
IOTHUB_SUBSCRIBE_TOPIC = "devices/{clientid}/messages/devicebound/#".format(clientid = IOTHUB_CLIENTID)

