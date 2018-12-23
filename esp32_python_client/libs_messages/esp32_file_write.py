import sys
import serial
import time
import msgpack
import binascii
import json
import crcmod
import time
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
       temp = self.configuration
       if b"ibeacon" in temp:
           beacon_name = self.configuration[b"ibeacon"][b"beacon_name"]
       
           print("beacon name",len(beacon_name),beacon_name)
           assert len(beacon_name) == 16
           access_dict = {}
           access_dict["beacon_name"] = beacon_name
           self.mess_gen.request_write_file(b"/spiffs/IBEACON.MPK",access_dict)
      
  def write_wifi_setup(self):
      temp = self.configuration
      if b"wifi" in temp:
          temp = self.configuration[b"wifi"]
          self.mess_gen.request_write_file(b"/spiffs/WIFI.MPK",temp)
       
       
  def write_mqtt_setup(self):
       temp = self.configuration
       if b"mqtt" in temp:
           temp = self.configuration[b"mqtt"]
           self.mess_gen.request_write_file( b"/spiffs/MQTT.MPK",temp)
       
  def write_io_output_setup(self):
       temp = self.configuration
       
       if b"d_outputs" in temp:

           data = temp[b"d_outputs"]
           self.mess_gen.request_write_file( "/spiffs/IO_OUT.MPK",data)
           
           
  def write_io_input_setup(self):
       temp = self.configuration
       
       if b"d_inputs" in temp:

           data = temp[b"d_inputs"]
           self.mess_gen.request_write_file( "/spiffs/IO_INPUT.MPK",data)
          
           
  def write_pwm_setup(self):
       tenp = self.configuration
       if b"d_pwm_outputs" in temp:
           data = temp[b"d_pwm_outputs"]
           self.mess_gen.request_write_file( "/spiffs/IO_PWM.MPK",data)

  def write_counter_setup(self):
       tenp = self.configuration
       if b"d_counter_inputs" in temp:
           data = temp[b"d_counter_inputs"]
           self.mess_gen.request_write_file( "/spiffs/IO_PULSE.MPK",data)   
           
  def write_dac_setup(self):
       tenp = self.configuration
       if b"a_dac_outputs" in temp:
           data = temp[b"a_dac_outputs"]
           self.mess_gen.request_write_file("/spiffs/IO_DAC.MPK",data)
           
  def write_ad_setup(self):
       tenp = self.configuration
       if b"a_ad_inputs" in temp:
           data = temp[b"a_ad_inputs"]
           self.mess_gen.request_write_file("/spiffs/IO_ADC1.MPK",data)              

  def write_lua_task_configuration(self):
       temp = self.configuration
       
       if b"LUA_TASKS" in temp:
           data = temp[b"LUA_TASKS"]
           self.mess_gen.request_write_file("/spiffs/LUA_TASKS.LUA",data)

  def write_lua_files(self):
       temp = self.configuration
       
       if b"LUA_FILES" in temp:
           data = temp[b"LUA_FILES"]
           for i in data:
              f= open("lua_files/"+i)
              data = f.read()
              f.close()
              data = data.encode()
             
              self.mess_gen.request_text_write_file("/spiffs/"+i,data)
              time.sleep(1)
              
              
  def write_modbus_relay(self):
      temp = self.configuration

      if b"MODBUS_RELAY" in temp:
     
           data = temp[b"MODBUS_RELAY"]
           self.mess_gen.request_write_file("/spiffs/MD_RELAY.MPK",data)          

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