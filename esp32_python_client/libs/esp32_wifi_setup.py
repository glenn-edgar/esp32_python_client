
from .esp32_commands_py3 import ESP32_Message_Generator


class ESP32_WIFI_MANAGER(object):

   def __init__(self,serial_handle):
       self.mess_gen = ESP32_Message_Generator(serial_handle)
       
   def write_wifi_setup(self):
       
       access_dict = {}
       access_dict["ssid"] = "onyx_1_G"
       access_dict["password"] = "read2go"
       access_dict["hostname"] = "esp32_slave"
       self.mess_gen.request_write_file("/spiffs/WIFI.MPK",access_dict)
      