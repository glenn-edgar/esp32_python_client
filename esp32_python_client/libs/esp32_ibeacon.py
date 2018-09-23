
from .esp32_commands_py3 import ESP32_Message_Generator
import binascii

class ESP32_IBEACON_MANAGER(object):

   def __init__(self,serial_handle):
       self.mess_gen = ESP32_Message_Generator(serial_handle)
       
   def write_ibeacon_setup(self,beacon_name):
       print("beacon name",len(beacon_name),beacon_name)
       assert len(beacon_name) == 16
       
       access_dict = {}
       access_dict["beacon_name"] = beacon_name
       self.mess_gen.request_write_file("/spiffs/IBEACON.MPK",access_dict)
      