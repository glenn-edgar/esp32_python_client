
from .esp32_commands_py3 import ESP32_Message_Generator
import binascii

class ESP32_MQTT_MANAGER(object):

   def __init__(self,serial_handle):
       self.mess_gen = ESP32_Message_Generator(serial_handle)
       
   def write_mqtt_setup(self,file_name,host,port,user_name,password,base_topic):
       
       
       access_dict = {}
       access_dict["PORT"] = port
       access_dict["HOST"] = host
       access_dict["USER_NAME"] = user_name
       access_dict["PASSWORD"] = password
       access_dict["BASE_TOPIC"] = base_topic
       self.mess_gen.request_write_file(file_name,access_dict)
      

 