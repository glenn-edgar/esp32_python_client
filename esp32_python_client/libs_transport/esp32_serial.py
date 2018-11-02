
import serial
import time
import msgpack
import binascii
import json
import crcmod

from threading import Thread

class Serial_Port_Manager(object):
   def __init__(self,comm_port):
       self.packet_recieved = False
       self.comm_port = comm_port
       self.stop_flag = False
       self.mac_cb = None
       self.file_read_cb = None   
       self.open()
       self.start()
       
   def get_packet_recieved(self):
       return self.packet_recieved

   def set_packet_recieved(self,value):
       self.packet_recieved = value

       
   def open( self):
       self.crc16 = crcmod.mkCrcFun(	0x11021, 0xffff, False, 0)
       ser = serial.Serial(
                        port=self.comm_port,
                        baudrate=115200,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout = None
                       )
       self.handle = ser
       return ser.isOpen()
       
   def close(self):
      self.handle.close()

   def write_packet(self,message):
     crc16_bin = self.crc16(message)
     crc_16_str = '{0:x}'.format(crc16_bin)     
     if len(crc_16_str) != 4:
         crc_16_str = "0"+crc_16_str
     ascii_packet = binascii.hexlify(message)+crc_16_str.encode()+b'\n'
     #print("crc ascii",crc_16_str)
     #print("len ",len(ascii_packet))
     #print("out     ascii_packet --->",ascii_packet)
     self.handle.write(ascii_packet)
       
      
   def read_packet(self):
       
        packet =[]
        
        x = b''
        while len(x) < 3 :
          if self.stop_flag == True:
              break
          x = self.handle.readline()
        
   
        return x[:-2]
 

   def stop(self):
       self.stop_flag = True
 
   def detect_command(self,packet):
       #print(packet)
       front_end = packet[0:8]
       
       if front_end != b'MSGPACK:':
          return False
       back_end = packet[-4:]
       if back_end != b':END' :
         return False
       
       hex_packet = packet[8:-8]
       binary_packet = binascii.unhexlify(hex_packet)
       #print("binary input packet----->",binary_packet)
       hex_crc =(self.crc16(binary_packet))
       
       crc_packet = int(packet[-8:-4], 16)
       #print("crc check",hex_crc,crc_packet)
       if hex_crc == crc_packet:
           try:
              print("cccc",binary_packet)
              x = msgpack.unpackb(binary_packet)
              print(x)
              temp_flag = x[b"TOPIC"]==b'COMMAND_RESPONSE'
              
              if temp_flag:
                 
                 if (x[b"COMMAND"] == b"FILE_READ"): 
                     
                     if self.file_read_cb != None:
                          if x[b"DATA"][b"FILE_DATA"] != None:
                               try:
                                 self.file_read_cb( x[b"DATA"][b"FILE_NAME"], msgpack.unpackb(x[b"DATA"][b"FILE_DATA"]))
                               except:
                                   pass
              if temp_flag:
                 if (x[b"COMMAND"] == b"WIFI_MAC_ADDRESS"): 
                    
                     if self.mac_cb != None:
                          self.mac_cb( x[b"DATA"])  
              self.packet_recieved = True
              
           except:
               raise #print("bad message pack")
        
           return True
       else:
          print("bad crc check",hex_crc,crc_packet)
          return False           
  
    
 
   def read_control(self):
       while(True):
          if self.stop_flag == True:
              break
          packet = self.read_packet()
          if self.stop_flag == True:
              break
          if self.detect_command(packet) == False:
              print(packet)


   def start(self):
         t = Thread(target=self.read_control, args=())
         t.start()
         

