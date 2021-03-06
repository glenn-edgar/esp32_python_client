
import serial
import time
import msgpack
import binascii
import json
import crcmod
from libs.esp32_commands_py3 import ESP32_Message_Generator
from libs.esp32_wifi_setup import ESP32_WIFI_MANAGER
from threading import Thread

class Serial_Port_Manager(object):
   def __init__(self):
       self.packet_recieved = False
   
   def get_packet_recieved(self):
       return self.packet_recieved

   def set_packet_recieved(self,value):
       self.packet_recieved = value

       
   def open( self,comm_port ):
       self.crc16 = crcmod.mkCrcFun(	0x11021, 0xffff, False, 0)
       ser = serial.Serial(
                        port=comm_port,
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
       self.handle.write(message)   
      
   def read_packet(self):
       
        packet =[]
        
        x = b''
        while len(x) < 3 :
           x = self.handle.readline()
        
   
        return x[:-2]
 

 
 
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
              x = msgpack.unpackb(binary_packet)
              print(x)
              #print(x[b"TOPIC"])
              if x[b"TOPIC"] == b"COMMAND_RESPONSE":
                 if (x[b"COMMAND"] == b"FILE_READ"): #and(x[b"DATA"][b"FILE_DATA"] != None ):
                      if x[b"DATA"][b"FILE_DATA"] != None:
                         print("####",msgpack.unpackb(x[b"DATA"][b"FILE_DATA"]))
              self.packet_recieved = True
              
           except:
               print("bad message pack")
        
           return True
       else:
          print("bad crc check",hex_crc,crc_packet)
          return False           

    
 
   def read_control(self):
       while(True):
      
          packet = self.read_packet()
         
          if self.detect_command(packet) == False:
              print(packet)


   def start(self):
         t = Thread(target=self.read_control, args=())
         t.start()
         

if __name__ == "__main__": 
   print("starting program") 
   
   esp_serial = Serial_Port_Manager()
   msg_generator = ESP32_Message_Generator(esp_serial)
   wifi_manager = ESP32_WIFI_MANAGER(esp_serial)
   print("opening setial port")
   esp_serial.open("COM5")
   print("starting thread \n")
   esp_serial.start()
  

   while(1):
    time.sleep(1)
    if esp_serial.packet_recieved == True:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ starting loop @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        msg_generator.request_list_commands()

        msg_generator.request_wifi_mac()
        time.sleep(3)
        msg_generator.request_heap_space()
        time.sleep(.3)
        wifi_manager.write_wifi_setup("esp_32_switches")
        time.sleep(1)
        msg_generator.request_list_directory("/spiffs/")
        time.sleep(.3)         
        msg_generator.request_read_file("/spiffs/WIFI.MPK")
        time.sleep(.3)
        exit()
    
        '''
        msg_generator.request_rename_file("/spiffs/WIFI.MPK","/spiffs/WIFI.BKK")
        time.sleep(1)
        msg_generator.request_list_directory("/spiffs")
        time.sleep(.3)
        msg_generator.request_delete_file("/spiffs/WIFI.BKK")
        time.sleep(1)
 
        msg_generator.request_list_directory("/spiffs")
        time.sleep(.3)
        #msg_generator.format_spiff_drive()
        #time.sleep(60)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ending @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        #print("list commands")
        #msg_generator.request_list_commands()
        #time.sleep(.3)
         #time.sleep(60)
        #msg_generator.request_list_directory("/spiffs/")
        #time.sleep(1)  
        #wifi_manager.write_wifi_setup()
        #time.sleep(1)
        '''
        '''
        #time.sleep(3)
        #msg_generator.request_reboot()
        #time.sleep(3)
        #esp_serial.set_packet_recieved(False)
      
        #print("read file")
        #msg_generator.format_spiff_drive()
        #time.sleep(60)
        msg_generator.request_list_directory("/spiffs/")
        time.sleep(1)
 
        wifi_manager.write_wifi_setup()
        time.sleep(1)
 
        msg_generator.request_list_directory("/spiffs/")

        time.sleep(1)
        msg_generator.request_read_file("/spiffs/WIFI.MPK")
        time.sleep(1)
        msg_generator.request_read_file("WIFI.MPK")
        
        time.sleep(1)
        msg_generator.request_delete_file("/spiffs/WIFI.MPK")
        time.sleep(1)
        msg_generator.request_delete_file("WIFI.MPK")
        time.sleep(1)
        msg_generator.request_list_directory("/spiffs/")
        time.sleep(1)
        print("$$$$$$$$$$$$$$$$$$$$$ Done $$$$$$$$$$$$$$$$$$$$$$$$$ ")
       
        #wifi_manager.write_wifi_setup()
        #msg_generator.request_read_file("/spiffs/WIFI.MPK")
        time.sleep(30)
   
        #print("wifi setup")
        #wifi_manager.write_wifi_setup()
        #time.sleep(2)   

        wifi_manager.write_wifi_setup()
        time.sleep(1)
        
        msg_generator.request_list_directory("/spiffs/")
        time.sleep(1)
        msg_generator.request_rename_file("/spiffs/WIFI.MPK","/spiffs/WIFI.BKK")
        
        time.sleep(1)
        msg_generator.request_read_file("/spiffs/WIFI.BKK")
        time.sleep(1)
        msg_generator.request_read_delete("/spiffs/WIFI.BKK");
        time.sleep(1)
        msg_generator.request_list_directory("/spiffs/")
        '''
        time.sleep(1)
 
        
        