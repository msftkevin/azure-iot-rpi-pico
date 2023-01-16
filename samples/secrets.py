#------------------------------------------------------------------------------
# WiFi Settings
SSID = '<SSID>'
PASSWORD = '<SSID_PASSWORD>'
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# IoT Hub Settings
# Use the following values to configure your IoT Hub connection 
# Replace the following items with your IoT Hub values
# <IOTHUB_CLIENTID> :   This is the 'Device ID' from your IoT Hub Device
# <IOTHUB_HOSTNAME> :   This is the 'Hostname' from your IoT Hub Overview tab
# <IOTHUB_PASSWORD> :   This is the 'Connection string with SAS token'.
#                       The connection string must be generated, which can be done
#                       with the Azure IoT Hub Explorer.
#                       https://learn.microsoft.com/en-us/azure/iot-fundamentals/howto-use-iot-explorer
IOTHUB_CLIENTID = '<CLIENT_ID>'
IOTHUB_HOSTNAME = '<IOT_HUB_HOSTNAME>'
IOTHUB_PASSWORD = '<SHARED_ACCESS_SIGNATURE_TOKEN>'
IOTHUB_USERNAME = '{hostname}/{clientid}/?api-version=2021-04-12'.format(hostname = IOTHUB_HOSTNAME, clientid = IOTHUB_CLIENTID)
IOTHUB_TOPIC_PUB = b'devices/{clientid}/messages/events/'.format(clientid = IOTHUB_CLIENTID)

# IoT Hub using MQTT Port 8883 for secure connection
# Leave IOTHUB_PORT_NO = 0 and the connection will default to 8883
IOTHUB_PORT_NO = 0
IOTHUB_SUBSCRIBE_TOPIC = "devices/{clientid}/messages/devicebound/#".format(clientid = IOTHUB_CLIENTID)
IOTHUB_TOPIC_MSG = b'{"buttonpressed":"1"}'
#------------------------------------------------------------------------------
