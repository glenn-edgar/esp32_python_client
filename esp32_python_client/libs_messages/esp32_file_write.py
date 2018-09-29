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
from threading import Thread


class FILE_TRANSFER(object):

  def __init__(self,transport, configuration):
       self.mess_gen = ESP32_Message_Generator(transport)
       self.configuration = configuration
       self.present = {}
       self.present[b"ibeacon"] = False
       self.present[b"wifi"] = False
       self.present[b"mqtt"] = False
       self.present["mac"] = False   
       self.data_check = {}
       self.data_check[b"ibeacon"] = False
       self.data_check[b"wifi"] = False
       self.data_check[b"mqtt"] = False
       self.data_check["mac"] = False   
       transport.mac_cb = self.mac_call_back
       transport.file_read_cb = self.file_read_callback       
       
  def write_ibeacon_setup(self):
       beacon_name = self.configuration[b"ibeacon"][b"beacon_name"]
       
       print("beacon name",len(beacon_name),beacon_name)
       assert len(beacon_name) == 16
       access_dict = {}
       access_dict["beacon_name"] = beacon_name
       self.mess_gen.request_write_file(b"/spiffs/IBEACON.MPK",access_dict)
      
  def write_wifi_setup(self):
       temp = self.configuration[b"wifi"]
       self.mess_gen.request_write_file(b"/spiffs/WIFI.MPK",temp)
       
       
  def write_mqtt_setup(self):
       temp = self.configuration[b"mqtt"]
       self.mess_gen.request_write_file( b"/spiffs/MQTT.MPK",temp)
       
  def file_read_callback( self, filename, file_data):
       
       if filename  ==  b"/spiffs/IBEACON.MPK":
          
           self.present[b"ibeacon"] = True
           self.data_check[b"ibeacon"] = self.verify_data(b"ibeacon",file_data)
       if filename  ==  b"/spiffs/WIFI.MPK":
           
           self.present[b"wifi"] = True
           self.data_check[b"wifi"] = self.verify_data(b"wifi",file_data)
       if filename  ==   b"/spiffs/MQTT.MPK":
          
          self.present[b"mqtt"] = True
          self.data_check[b"mqtt"] =  self.verify_data(b"mqtt",file_data)
       
           
  def mac_call_back(self,mac_address):
        print("mac cb",mac_address,self.configuration["mac"])
        self.present["mac"] = True
        if mac_address != self.configuration["mac"]:
           self.data_check["mac"] = False
        else:
            self.data_check["mac"] = True
            
  def verify_data(self,key,input_data):
       
       ref_data = self.configuration[key]
       for key,data in ref_data.items():
           if input_data[key] != data:
               
               return False
       
       return True
        
  def verify_presence(self):
       
       for key,data in self.present.items():
           if data == False:
               return False
       return True
  
  def verify_data_all(self):
        for key,data in self.data_check.items():
           if data == False:
               
               return False
        return True