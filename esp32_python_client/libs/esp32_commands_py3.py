import msgpack
import crcmod
import binascii
class ESP32_Message_Generator(object):

  def __init__(self,serial_handle):
        self.serial_handler = serial_handle
        self.crc16 = crcmod.mkCrcFun(	0x11021, 0xffff, False, 0)

        
  def request_wifi_mac(self):
      request = {}
      request["COMMAND"] = "GET_WIFI_MAC_ADDRESS"
      request["DATA"] = "N/A"
      self.send_request(request)      


  def request_list_commands(self):
      request = {}
      request["COMMAND"] = "LIST_COMMANDS"
      request["DATA"] = "N/A"
      self.send_request(request)      

  def request_reboot(self):
      request = {}
      request["COMMAND"] = "REBOOT"
      request["DATA"] = "N/A"
      self.send_request(request)

  def request_write_file(self,file_name,data):
      request = {}
      request["COMMAND"] = "FILE_WRITE"
      request["DATA"] = {"FILE_NAME":file_name, "FILE_DATA":data}
      print("write_file",file_name,request)
      self.send_request(request)

  def request_list_directory(self):
         
      request = {}
      request["COMMAND"] = "FILE_DIR"
      request["DATA"] = "N/A"
      self.send_request(request)   
      
  def send_request(self,msg_dict):
     binary_data = msgpack.packb(msg_dict, use_bin_type=True)
     crc16_bin = self.crc16(binary_data)
     crc_16_str = '{0:x}'.format(crc16_bin)     
     ascii_packet = binascii.hexlify(binary_data)+crc_16_str.encode()+b'\n'
     print("ascii_packet",ascii_packet)
     print(self.serial_handler.handle.write(ascii_packet))