
import sys
import time
import msgpack
import binascii
import json
import crcmod
from libs_messages.esp32_commands_py3 import ESP32_Message_Generator

from libs_transport.esp32_serial import Serial_Port_Manager
from threading import Thread


def instanciate_transport():
    length  = len(sys.argv)
    assert length > 1
    return Serial_Port_Manager(sys.argv[1])         



if __name__ == "__main__": 
   print("starting program") 
   
   esp_serial = instanciate_transport()
   msg_generator = ESP32_Message_Generator(esp_serial)
   

  

   while(1):
    time.sleep(1)
    if esp_serial.packet_recieved == True:
        time.sleep(3)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ starting loop @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        msg_generator.request_list_commands()

        msg_generator.request_wifi_mac()
        time.sleep(3)
        msg_generator.request_heap_space()
        time.sleep(.3)
        msg_generator.request_list_directory("/spiffs/")
        time.sleep(.3)         
 
        time.sleep(1)
 
        
        