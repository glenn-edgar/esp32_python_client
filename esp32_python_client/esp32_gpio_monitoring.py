import sys
import msgpack
import binascii
import json
import crcmod
import paho.mqtt.client as mqtt
import ssl
import time
from libs_messages.esp32_gpio_commands import ESP32_Message_Generator
from libs_transport.esp_mqtt import MQTT_CLIENT

class MQTT_TX_TRANSPORT(object):
    def __init__(self,mqtt_class,base_topic):
        self.mqtt_class = mqtt_class
        self.base_topic = base_topic
       

    def change_topic(self,base_topic):
        self.base_topic = base_topic

    def write_packet(self,payload,topic):
        print("base topic",self.base_topic)
        print("topic",topic)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$",self.base_topic+topic)
        self.mqtt_class.publish(self.base_topic+topic,payload)


def instanciate_transport():
    length  = len(sys.argv)
    if length >5:
       return MQTT_CLIENT( sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]  ) #ip,port,username,password
    else:
        print("usage is esp32_monitor_mqtt.py ip port username  password topic ")
        exit()

if __name__ == "__main__": 
    mqtt_class = instanciate_transport()
    transport = MQTT_TX_TRANSPORT(mqtt_class,sys.argv[5])
    gpio_message = ESP32_Message_Generator(transport)
    mqtt_class.start()
    while mqtt_class.is_connected() == False:
        time.sleep(1)
    print("mqtt is connectoed")
    #gpio_message.read_gpio_pins([23,22,21,19,18,5,17,16])
    gpio_message.write_gpio_pins([23,22,21,19,18,5,17,16],[0,0,0,0 ,0,0,0,0])