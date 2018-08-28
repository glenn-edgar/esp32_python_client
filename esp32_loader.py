
import serial
import time
import msgpack
import binascii
import json
from threading import Thread

class Serial_Port_Manager(object):
   def open( self,comm_port ):
    
       ser = serial.Serial(
                        port=comm_port,
                        baudrate=115200,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout = .05
                       )
       self.handle = ser
       return ser.isOpen()
       
   def close(self):
      self.handle.close()

   def read_packet(self):
       
        packet =[]
        x=""
        while(x !="\n" ):
        
            x = self.handle.read(size=1)
           
            if len(x) and (x != "\n") and (x != "\r") != 0:
               packet.append(x)    
        return "".join(packet)
 
# BASE64:
   def detect_command(self,packet):
      
       front_end = packet[0:7]
       if front_end != "BASE64:":
          return False
       back_end = packet[-4:]
       if back_end != ":END" :
         return False
      
       hex_packet = packet[7:-4]
       
       binary_packet = binascii.unhexlify(hex_packet)
       

      
       x = msgpack.unpackb(binary_packet)
       print("packet detected --->",json.dumps(x))
       return True      
 
def read_packet(esp_serial):
  while(True):
      packet = esp_serial.read_packet()
      if esp_serial.detect_command(packet) == False:
         print(packet)
 

      
      
      
if __name__ == "__main__": 
   print("starting program") 
   esp_serial = Serial_Port_Manager()
   print("opening setial port")
   esp_serial.open("COM4")
   print("starting thread \n")
   t = Thread(target=read_packet, args=(esp_serial,))
   t.start()
   while(True):
     time.sleep(1)