import network
import time
import machine
import secrets

from umqtt.simple import MQTTClient
from machine import Pin
   
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
 
# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
 
led = machine.Pin('LED', machine.Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

def mqtt_connect():
    # To connect to Azure IoT services we must use a Secure Cert
    certificate_path = "baltimore.cer"
    print('Loading Blatimore Certificate')
    with open(certificate_path, 'r') as f:
        cert = f.read()
    print('Obtained Baltimore Certificate')
    sslparams = {'cert':cert}
    
    client = MQTTClient(client_id=secrets.IOTHUB_CLIENTID, server=secrets.IOTHUB_HOSTNAME, port=secrets.IOTHUB_PORT_NO, user=secrets.IOTHUB_USERNAME, password=secrets.IOTHUB_PASSWORD, keepalive=3600, ssl=True, ssl_params=sslparams)
    client.connect()
    
    print('Connected to IoT Hub MQTT Broker')
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

def callback_handler(topic, message_receive):
    print("Received message")
    print(message_receive)
    if message_receive.strip() == b'led_on':
        led.value(1)
    else:
        led.value(0)


# Setup
try:
    client = mqtt_connect()
    client.set_callback(callback_handler)
    client.subscribe(topic=secrets.IOTHUB_SUBSCRIBE_TOPIC)
except OSError as e:
    reconnect()

# Successful connection to MQTT
led.value(1)
time.sleep(1)
led.value(0)

while True:
    
    client.check_msg()
    
    if button.value():
        client.publish(secrets.IOTHUB_TOPIC_PUB, secrets.IOTHUB_TOPIC_MSG)
        time.sleep(0.5)
    else:
        client.publish(secrets.IOTHUB_TOPIC_PUB, '{"buttonpressed": "0"}')
        time.sleep(5)