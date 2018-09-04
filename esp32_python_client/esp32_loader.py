
import serial
import time
import msgpack
import binascii
import json
import crcmod

from threading import Thread

class Serial_Port_Manager(object):
   def __init__(self):
       self.packet_recieved = False
       
   def open( self,comm_port ):
       self.crc16 = crcmod.mkCrcFun(	0x11021, 0xffff, False, 0)
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
       print(packet)
       front_end = packet[0:8]
       
       if front_end != "MSGPACK:":
          return False
       back_end = packet[-4:]
       if back_end != ":END" :
         return False
       
       hex_packet = packet[8:-8]
       binary_packet = binascii.unhexlify(hex_packet)
       hex_crc =(self.crc16(binary_packet))
       
       crc_packet = int(packet[-8:-4], 16)
       print("crc check",hex_crc,crc_packet)
       if hex_crc == crc_packet:
           try:
              x = msgpack.unpackb(binary_packet)
           except:
               print("bad message pack")
           try:
               print("packet detected --->",json.dumps(x))
               self.packet_recieved = True
           except:
              print("not a json packet")           
           return True
       return False           

    
 
   def read_control(self):
       while(True):
      
          packet = self.read_packet()
    
          if self.detect_command(packet) == False:
             pass #print(packet)


   def start(self):
         t = Thread(target=self.read_control, args=())
         t.start()
         
def send_wifi_setup( serial_handle):

    access_dict = {}
    access_dict["ssid"] = "onyx_1_G"
    access_dict["password"] = "read2go"
    access_dict["hostname"] = "esp32_slave"
    packed_object = msgpack.packb(access_dict, use_bin_type=True)
    crc16 = crcmod.mkCrcFun(	0x11021, 0xffff, False, 0)
    crc16_bin = crc16(packed_object)
    crc_16_str = '{0:x}'.format(crc16_bin)
    print(crc_16_str)
    ascii_packet = binascii.hexlify(packed_object)+crc_16_str+"\n"
    print(ascii_packet)
    print(len(ascii_packet))
    serial_handle.handle.write(ascii_packet)
      
if __name__ == "__main__": 
   print("starting program") 
   esp_serial = Serial_Port_Manager()
   print("opening setial port")
   esp_serial.open("COM4")
   print("starting thread \n")
   esp_serial.start()
   while(True):
     time.sleep(5)
     if esp_serial.packet_recieved == True:
        send_wifi_setup(esp_serial)
        