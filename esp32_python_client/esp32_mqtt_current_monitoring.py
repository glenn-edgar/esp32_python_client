import sys
import msgpack
import binascii
import json
import crcmod
import paho.mqtt.client as mqtt
import ssl
import time
from libs_messages.esp32_current_monitoring import ESP32_MQTT_Current_Message_Generator
from libs_transport.esp_mqtt import MQTT_CLIENT

class MQTT_TX_TRANSPORT(object):
    def __init__(self,mqtt_class,base_topic):
        self.mqtt_class = mqtt_class
        self.base_topic = "/REMOTES/"+base_topic
       

    def change_topic(self,base_topic):
        self.base_topic = base_topic

    def write_packet(self,payload,topic):
        #print("base topic",self.base_topic)
        #print("topic",topic)
        print("out --->",self.base_topic+topic)
        self.mqtt_class.publish(self.base_topic+topic,payload)


def instanciate_transport():
    length  = len(sys.argv)
    if length >5:
       return MQTT_CLIENT( sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]  ) #ip,port,username,password
    else:
        print("usage is esp32_mqtt_current_monitoring.py ip port username  password topic ")
        exit()

if __name__ == "__main__": 
    mqtt_class = instanciate_transport()
    transport = MQTT_TX_TRANSPORT(mqtt_class,sys.argv[5])
    mqtt_message = ESP32_MQTT_Current_Message_Generator(transport)
    mqtt_class.start()
    while mqtt_class.is_connected() == False:
        time.sleep(1)
    while(1):
        value = int(input())
        
        if value == 0:
            mqtt_message.read_max_currents()

        if value == 1:
            mqtt_message.clear_max_currents( )           
            
        if value == 2:
            mqtt_message.read_current()

        if value == 3:
            mqtt_message.enable_equipment_relay()   
            
        if value == 4:
            mqtt_message.enable_irrigation_relay()

        if value == 5:
            mqtt_message.disable_equipment_relay()            
            
        if value == 6:
            mqtt_message.disable_irrigation_irrigation()

        if value == 7:
            mqtt_message.read_relay_states()               