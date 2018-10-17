import msgpack


class ESP32_Message_Generator(object):

   def __init__(self,transport_handle):
        self.transport_handler = transport_handle
        

        
   def read_gpio_pins(self,gpio_pins):
      request = {}
      request["pins"] = gpio_pins
      request["topic"] = "INPUT/GPIO/READ"
      self.send_request(request)      

   def write_gpio_pins(self,gpio_pins,values):
      assert len(gpio_pins) == len(values),"write_gpio_pin parameter mismatch"
      request = {}
      request["pins"] = gpio_pins
      request["topic"] = "OUTPUTS/GPIO/SET"
      request["init_values"] = values
      self.send_request(request)      


   def write_gpio_pulse(self, pulse_pin,starting_value,ending_value,time_tick):
       request = {}
       request["topic"] = "OUTPUTS/GPIO/SET_PULSE"
       request["PULSE_PIN"] = pulse_pin
       request["PULSE_STARTING_VALUE"] = starting_value
       request["PULSE_ENDING_VALUE"] = ending_value
       request["PULSE_TIME_TICK"] = time_tick
       self.send_request(request)


   def send_request(self,msg_dict):
     print("msg_dict",msg_dict)
     binary_data = msgpack.packb(msg_dict, use_bin_type=True)
     self.transport_handler.write_packet(binary_data,msg_dict["topic"])

