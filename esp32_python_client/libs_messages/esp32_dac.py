import msgpack

class ESP32_DAC_Message_Generator(object):

   def __init__(self,transport_handle):
        self.transport_handler = transport_handle
        self.buffer_array = None

        
   def read_dac_values(self):
      request = {}
     
      request["topic"] = "OUTPUTS/DAC/REQUEST_OUTPUT"
      self.send_request(request)      

   def clear_dac_buffer(self):
       self.buffer_array= []
       
   def write_dac_value(self,index, value ):
       temp = {}
       temp["index"] = index
       temp["value"] = value
       self.buffer_array.append(temp) 
    
   def write_dac(self):
      request = {}
      request["topic"] = "OUTPUTS/DAC/CHANGE_OUTPUT"
      request["DAC_OUTPUTS"] = []
      for i in self.buffer_array:
         request["DAC_OUTPUTS"].append(i) 
      self.send_request(request)   
      self.buffer_array = None      
            
 


  
   def send_request(self,msg_dict):
     print("msg_dict",msg_dict)
     binary_data = msgpack.packb(msg_dict, use_bin_type=True)
     self.transport_handler.write_packet(binary_data,msg_dict["topic"])