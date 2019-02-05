
import msgpack
class ESP32_MQTT_Current_Message_Generator(object):

   def __init__(self,transport_handle):
        self.transport_handler = transport_handle
        
   def  read_current_limit(self):
      request = {}
      request["topic"] = "INPUT/MQTT_CURRENT/GET_LIMIT_CURRENTS"
      self.send_request(request)   
 
   def read_max_currents(self):
      request = {}
      request["topic"] = "INPUT/MQTT_CURRENT/GET_MAX_CURRENTS"
      self.send_request(request)   
      

   def clear_max_currents(self):
      request = {}
      request["topic"] = "INPUT/MQTT_CURRENT/CLEAR_MAX_CURRENTS"
      self.send_request(request)   
      

   def read_current(self):
      request = {}
      request["topic"] = "INPUT/MQTT_CURRENT/READ_CURRENT"
      self.send_request(request)   

   def enable_equipment_relay(self):
      request = {}
      request["topic"] = "OUTPUT/MQTT_CURRENT/ENABLE_EQUIPMENT_RELAY"
      self.send_request(request)   

   def enable_irrigation_relay(self):
      request = {}
      request["topic"] = "OUTPUT/MQTT_CURRENT/ENABLE_IRRIGATION_RELAY"
      self.send_request(request)   

   def disable_equipment_relay(self):
      request = {}
      request["topic"] = "OUTPUT/MQTT_CURRENT/DISABLE_EQUIPMENT_RELAY"
      self.send_request(request)   

   def disable_irrigation_irrigation(self):
      request = {}
      request["topic"] = "OUTPUT/MQTT_CURRENT/DISABLE_IRRIGATION_RELAY"
      self.send_request(request)   

   def read_relay_states(self):
      request = {}
      request["topic"] = "OUTPUT/MQTT_CURRENT/READ_RELAY_STATES"
      self.send_request(request)   
  

 


   def send_request(self,msg_dict):
     print("msg_dict",msg_dict)
     binary_data = msgpack.packb(msg_dict, use_bin_type=True)
     self.transport_handler.write_packet(binary_data,msg_dict["topic"])

