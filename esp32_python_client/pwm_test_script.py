import sys
import time
import msgpack
import binascii
import json
import crcmod
import paho.mqtt.client as mqtt
import ssl
from libs_messages.esp32_commands_py3 import ESP32_Message_Generator
from esp32_configuration_manager import *
from libs_messages.esp32_pwm_pulse import ESP32_PWM_Message_Generator

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
    pwm_messages = ESP32_PWM_Message_Generator(transport)
    
    mqtt_class.start()
    while mqtt_class.is_connected() == False:
        time.sleep(1)
    print("mqtt is connectoed")
    time.sleep(3)
    pwm_messages.read_pwm_pins()
    time.sleep(5)
    
    pwm_messages.clear_pwm_buffer()
    pwm_messages.write_pwm_timer(0,90.,10.)
    pwm_messages.write_pwm_timer(1,.3,.7)
    pwm_messages.write_pwm()
    time.sleep(1)
    pwm_messages.read_pwm_pins()