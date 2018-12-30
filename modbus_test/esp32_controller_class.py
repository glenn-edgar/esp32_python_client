#
#
#  File: io_controller_class.py
#
#
#
#
#

import struct    

import time





class Esp32_Controller_Base_Class(object):
    
   def __init__(self,instrument, click_io = [], m_tags = {}):
       
       self.instrument  = instrument
       self.click_reg_address = {}
       self.click_bit_address = {}
       self.click_io          = click_io
   
       m_tags["turn_on_valves"] = self.turn_on_valves
       m_tags["turn_off_valves"] = self.turn_off_valves
       m_tags["load_duration_counters"] = self.load_duration_counters
       m_tags["clear_duration_counters"] = self.clear_duration_counters
       m_tags["read_mode_switch"]        = self.read_mode_switch
       m_tags["read_mode"]               = self.read_mode
       m_tags["read_wd_flag"]            = self.read_wd_flag
       m_tags["write_wd_flag"]           = self.write_wd_flag
       m_tags["read_input_bit"]          = self.read_input_bit
       self.m_tags = m_tags
       self.disable_reg                  = 2
       self.load_duration_reg            = 1
       self.wd_flag_reg                  = 0
      

 
       
   def disable_all_sprinklers( self, modbus_address ):
      
      
      self.instrument.write_registers(modbus_address,self.disable_reg,  [1] )




   def turn_on_valves( self, modbus_address, input_list ):
      
       for valve in input_list:  
          self.instrument.write_bits( modbus_address, valve,[0])

   def turn_off_valves( self,  modbus_address, input_list  ):
          
       for valve in input_list:  
          valve           = valve 
          self.instrument.write_bits( modbus_address,valve,[1])


   def load_duration_counters( self, modbus_address, input_list  ):
        duration = input_list[0]
        self.instrument.write_registers(modbus_address,self.load_duration_reg, [duration] )


       
                         
   def clear_duration_counters( self, modbus_address  ):
        duration = 0
        self.instrument.write_registers(modbus_address,self.load_duration_reg, [duration] )

   def read_duration_counters( self, modbus_address  ):
        
        return self.instrument.read_registers(modbus_address,self.load_duration_reg, 1 )

   def read_input_bit( self, modbus_address, input_list ):
      
      read_bit      = input_list[0]
     
      return self.instrument.read_bits(modbus_address, read_bit,1 )[0]


   def read_mode_switch( self, modbus_address ):
      
      return 1 # no mode switch

   def read_mode( self, modbus_address ):
      # mode is always on

      return 1

  
   def read_wd_flag( self, modbus_address ):
      print("wd_flag_reg",self.wd_flag_reg)
      return self.instrument.read_registers( modbus_address, self.wd_flag_reg,1 )[0]
      

   def write_wd_flag( self, modbus_address ):
      
      self.instrument.write_registers( modbus_address, self.wd_flag_reg,[1])

      
if __name__ == "__main__":
   import sys
   print("made it here")
   from modbus_driver.new_instrument_serial import new_instrument
   address= int(sys.argv[2])
   instrument = new_instrument(com_port = sys.argv[1])
   esp32_serial_driver = Esp32_Controller_Base_Class(instrument)
   esp32_serial_driver.write_wd_flag(address)
   esp32_serial_driver.disable_all_sprinklers( address )
   esp32_serial_driver.load_duration_counters(address, [120]  )
   esp32_serial_driver.turn_on_valves(address,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 ] )
   time.sleep(10)
   #esp32_serial_driver.turn_off_valves(address,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 ] )
   #exit()
   while True:
      esp32_serial_driver.write_wd_flag(address)
      print(esp32_serial_driver.read_duration_counters(121))
      time.sleep(30)
   
   esp32_serial_driver.disable_all_sprinklers(address)
   time.sleep(1)
   esp32_serial_driver.clear_duration_counters(address)
   time.sleep(1)
   esp32_serial_driver.write_wd_flag(address)
   time.sleep(1)
   print(esp32_serial_driver.read_wd_flag(address))
    
  