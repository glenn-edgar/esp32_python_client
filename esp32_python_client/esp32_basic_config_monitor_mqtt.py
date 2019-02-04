
import time
import sys
import msgpack
import binascii
import json
import crcmod
import paho.mqtt.client as mqtt
import ssl
from libs_messages.esp32_file_write import FILE_TRANSFER
from libs_messages.esp32_commands_py3 import ESP32_Message_Generator
from esp32_configuration_manager import *

from libs_transport.esp_mqtt import MQTT_CLIENT

class MQTT_TX_TRANSPORT(object):
    def __init__(self,mqtt_class,tx_topic):
        self.mqtt_class = mqtt_class
        self.tx_topic = tx_topic

    def change_topic(self,topic):
        self.tx_topic = topic

    def write_packet(self,payload,topic):
        temp = msgpack.unpackb(payload)
        #print("$$$$$$$$$$$$$$$$$$$$$$$$$",self.tx_topic,topic, payload)
        
        self.mqtt_class.publish(self.tx_topic+topic,payload)


def instanciate_transport():
    length  = len(sys.argv)
    print("usage is esp32_monitor_mqtt.py configuration  ")
    if length >1:
       
        temp = remote_configuration[sys.argv[1]][b"mqtt"]
        ip = temp[b"HOST"].decode()
        port = temp[b"PORT"]
        username = temp[b"USER_NAME"].decode()
        password = temp[b"PASSWORD"].decode()
        topic = temp[b"BASE_TOPIC"].decode()
        print(ip,port,username,password,topic)
        return MQTT_CLIENT( ip,port,username,password,topic  ) #ip,port,username,password,topic     
    else:
        
        exit()

if __name__ == "__main__": 
    mqtt_class = instanciate_transport()
    topic = remote_configuration[sys.argv[1]][b"mqtt"][b"BASE_TOPIC"].decode()
    transport = MQTT_TX_TRANSPORT(mqtt_class,topic)
    msg_generator = ESP32_Message_Generator(transport,"BUILT_IN_CMD")
    file_write = FILE_TRANSFER(transport,remote_configuration[sys.argv[1]])
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
    file_write.write_current_monitor()