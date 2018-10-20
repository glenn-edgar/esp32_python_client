import msgpack

class ESP32_PWM_Message_Generator(object):

   def __init__(self,transport_handle):
        self.transport_handler = transport_handle
        self.buffer_array = None

        
   def read_pwm_pins(self):
      request = {}
     
      request["topic"] = "OUTPUTS/PWM/REQUEST_DUTY"
      self.send_request(request)      

   def clear_pwm_buffer(self):
       self.buffer_array= []
       
   def write_pwm_timer(self,timer_id, duty_a,duty_b ):
       temp = {}
       temp["timer_id"] = timer_id
       temp["duty_a"] = duty_a
       temp["duty_b"] = duty_b
       self.buffer_array.append(temp)
    
   def write_pwm(self):
      request = {}
      request["topic"] = "OUTPUTS/PWM/CHANGE_DUTY"
      request["PWM_OUTPUTS"] = []
      for i in self.buffer_array:
         request["PWM_OUTPUTS"].append(i) 
      self.send_request(request)   
      self.buffer_array = None      
            
 


  
   def send_request(self,msg_dict):
     print("msg_dict",msg_dict)
     binary_data = msgpack.packb(msg_dict, use_bin_type=True)
     self.transport_handler.write_packet(binary_data,msg_dict["topic"])