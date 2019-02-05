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
        try:
            temp = input()
            value = int(temp)
        except:
            value = temp
            
            
        if value == 'm':
           print("option 0 /REMOTES/CURRENT_MONITOR_1/INPUT/MQTT_CURRENT/GET_LIMIT_CURRENTS")
           print("option 1/REMOTES/CURRENT_MONITOR_1/INPUT/MQTT_CURRENT/GET_MAX_CURRENTS")
           print("option 2  /REMOTES/CURRENT_MONITOR_1/INPUT/MQTT_CURRENT/CLEAR_MAX_CURRENTS")
           print("option 3  /REMOTES/CURRENT_MONITOR_1/INPUT/MQTT_CURRENT/READ_CURRENT")
           print("option 4  /REMOTES/CURRENT_MONITOR_1/OUTPUT/MQTT_CURRENT/ENABLE_EQUIPMENT_RELAY")
           print("option 5  /REMOTES/CURRENT_MONITOR_1/OUTPUT/MQTT_CURRENT/ENABLE_IRRIGATION_RELAY")
           print("option 6  /REMOTES/CURRENT_MONITOR_1/OUTPUT/MQTT_CURRENT/DISABLE_EQUIPMENT_RELAY")
           print("option 7  /REMOTES/CURRENT_MONITOR_1/OUTPUT/MQTT_CURRENT/DISABLE_IRRIGATION_RELAY")
           print("option 8 /REMOTES/CURRENT_MONITOR_1/OUTPUT/MQTT_CURRENT/READ_RELAY_STATES")

        if value == 0:
            mqtt_message.read_current_limit()

        if value == 1:
            mqtt_message.read_max_currents()

        if value == 2:
            mqtt_message.clear_max_currents( )           
            
        if value == 3:
            mqtt_message.read_current()

        if value == 4:
            mqtt_message.enable_equipment_relay()   
            
        if value == 5:
            mqtt_message.enable_irrigation_relay()

        if value == 6:
            mqtt_message.disable_equipment_relay()            
            
        if value == 7:
            mqtt_message.disable_irrigation_irrigation()

        if value == 8:
            mqtt_message.read_relay_states()               