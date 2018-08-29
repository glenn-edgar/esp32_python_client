
import serial
import time
import msgpack
import binascii
import json
from threading import Thread

class Serial_Port_Manager(object):
   def __init__(self):
       self.packet_recieved = False

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

   def write_packet(self,message):
       self.handle.write(message)   
      
   def read_packet(self):
       
        packet =[]
        x=""
        while(x !="\n" ):
        
            x = self.handle.read(size=1)
           
            if len(x) and (x != "\n") and (x != "\r") != 0:
               packet.append(x)    
        return "".join(packet)
 

 
 
   def detect_command(self,packet):
      
       front_end = packet[0:7]
       if front_end != "BASE64:":
          return False
       back_end = packet[-4:]
       if back_end != ":END" :
         return False
       self.packet_recieved = True
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
 
def send_wifi_setup( serial_handle):
    access_dict = {}
    access_dict["ssid"] = "onyx_1_G"
    access_dict["password"] = "read2go"
    access_dict["hostname"] = "esp32_slave"
    packed_object = msgpack.packb(access_dict, use_bin_type=True)
    ascii_packet = binascii.hexlify(packed_object)+"\n"
    print(ascii_packet)
    serial_handle.handle.write(ascii_packet)
      
if __name__ == "__main__": 
   print("starting program") 
   esp_serial = Serial_Port_Manager()
   print("opening setial port")
   esp_serial.open("COM4")
   print("starting thread \n")
   t = Thread(target=read_packet, args=(esp_serial,))
   t.start()
   while(True):
     time.sleep(5)
     if esp_serial.packet_recieved == True:
        send_wifi_setup(esp_serial)
        