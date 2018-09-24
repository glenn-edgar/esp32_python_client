
import sys
import serial
import time
import msgpack
import binascii
import json
import crcmod
from esp32_configuration_manager import *

from libs_messages.esp32_commands_py3 import ESP32_Message_Generator
from libs_transport.esp32_serial import Serial_Port_Manager
from libs_messages.esp32_file_write import FILE_TRANSFER
from threading import Thread



     
if __name__ == "__main__": 
   print("starting program") 
   configuration, transport = instanciate_transport(remote_configuration )

   msg_generator = ESP32_Message_Generator(transport)
   file_transfer = FILE_TRANSFER( transport,configuration )

   print("starting thread \n")
   
  

   
   while(1):
    time.sleep(1)
    if transport.packet_recieved == True:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ starting transfoer @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        msg_generator.request_wifi_mac()
        time.sleep(1)
        if file_transfer.present["mac"] == False or file_transfer.data_check["mac"] == False:
            transport.stop()
            raise
        
        msg_generator.request_list_directory("/spiffs/")
        time.sleep(1)
        msg_generator.format_spiff_drive()
        time.sleep(15)
        msg_generator.request_list_directory("/spiffs/")
        time.sleep(1)

        transport.stop()
        exit()