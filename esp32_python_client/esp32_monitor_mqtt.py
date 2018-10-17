
import time
import sys
import msgpack
import binascii
import json
import crcmod
import paho.mqtt.client as mqtt
import ssl
from libs_messages.esp32_commands_py3 import ESP32_Message_Generator

from libs_transport.esp_mqtt import MQTT_CLIENT

class MQTT_TX_TRANSPORT(object):
    def __init__(self,mqtt_class,tx_topic):
        self.mqtt_class = mqtt_class
        self.tx_topic = tx_topic

    def change_topic(self,topic):
        self.tx_topic = topic

    def write_packet(self,payload,topic):
        temp = msgpack.unpackb(payload)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$",self.tx_topic,topic, payload)
       
        self.mqtt_class.publish(self.tx_topic+topic,payload)


def instanciate_transport():
    length  = len(sys.argv)
    if length >5:
       return MQTT_CLIENT( sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]  ) #ip,port,username,password,topic     
    else:
        print("usage is esp32_monitor_mqtt.py ip port username  password  ")
        exit()

if __name__ == "__main__": 
    mqtt_class = instanciate_transport()
    transport = MQTT_TX_TRANSPORT(mqtt_class,sys.argv[5])
    msg_generator = ESP32_Message_Generator(transport,"BUILT_IN_CMD")
    mqtt_class.start()
    while mqtt_class.is_connected() == False:
        time.sleep(1)
    print("mqtt is connectoed")
    msg_generator.request_wifi_mac()
    time.sleep(1)
    msg_generator.request_list_commands()
    time.sleep(2)
    msg_generator.request_heap_space()
    time.sleep(2)
    msg_generator.request_list_directory("/spiffs/")