
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



def instanciate_transport(configuration_data):
    length  = len(sys.argv)
    print("usaage  config_name")
    assert length > 1
    configuration  = configuration_data[sys.argv[1]]
    return configuration ,Serial_Port_Manager(configuration["com"])         


     
if __name__ == "__main__": 
   print("starting program") 
   configuration, transport = instanciate_transport(remote_configuration )

   msg_generator = ESP32_Message_Generator(transport)
   file_transfer = FILE_TRANSFER( transport,configuration )

   print("starting thread \n")
   
  

   
   while(1):
    time.sleep(1)
    if transport.packet_recieved == True:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ starting transfer @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        msg_generator.request_wifi_mac()
        time.sleep(1)
        if file_transfer.present["mac"] == False or file_transfer.data_check["mac"] == False:
            transport.stop()
            raise
        msg_generator.request_list_directory("/spiffs/")
        time.sleep(4)         
 
        time.sleep(1)
        file_transfer.write_wifi_setup()
        time.sleep(1)
        file_transfer.write_ibeacon_setup()
        time.sleep(1)
        file_transfer.write_mqtt_setup()
        time.sleep(1)
        file_transfer.write_io_input_setup()
        time.sleep(1)
        file_transfer.write_io_output_setup()
        time.sleep(1)
        file_transfer.write_pwm_setup()
        time.sleep(1)
        file_transfer.write_counter_setup()
        time.sleep(1)
        file_transfer.write_dac_setup()
        time.sleep(1)
        file_transfer.write_ad_setup()
        time.sleep(1)
        
        msg_generator.request_read_file("/spiffs/WIFI.MPK")
        time.sleep(1)
        msg_generator.request_read_file("/spiffs/IBEACON.MPK")
        time.sleep(1)
        msg_generator.request_read_file( "/spiffs/MQTT.MPK")
        time.sleep(1)
        msg_generator.request_read_file( "/spiffs/IO_INPUT.MPK")
        time.sleep(1)
        msg_generator.request_read_file( "/spiffs/IO_OUT.MPK")
        time.sleep(1)
        msg_generator.request_read_file( "/spiffs/IO_PWM.MPK")
        time.sleep(1)
        msg_generator.request_read_file( "/spiffs/IO_PULSE.MPK")
        

        time.sleep(1)
        msg_generator.request_read_file( "/spiffs/IO_DAC.MPK")

        time.sleep(1)
        msg_generator.request_read_file( "/spiffs/IO_ADC1.MPK")
        time.sleep(1)
        
        msg_generator.request_list_directory("/spiffs/")
        time.sleep(4)         
 
       
        if file_transfer.verify_data_all() == False or file_transfer.verify_presence() == False:
            raise
        time.sleep(1)
        msg_generator.request_reboot()
        time.sleep(15)
        transport.stop()
        exit()