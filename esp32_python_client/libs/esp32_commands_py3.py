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
      request["DATA"] = {"FILE_NAME":file_name,  "FILE_DATA":data}
      self.send_request(request)

  def request_read_file(self,file_name):
      request = {}
      request["COMMAND"] = "FILE_READ"
      request["DATA"] = {"FILE_NAME":file_name.encode()}
      
      self.send_request(request)
      
  def format_spiff_drive(self):
      request = {}
      request["COMMAND"] = "FORMAT_SPIFFS"
      request["DATA"] = "N/A"
      
      self.send_request(request)

      
      
  def request_delete_file(self,file_name):
      request = {}
      request["COMMAND"] = "FILE_DELETE"
      request["DATA"] = {"FILE_NAME":file_name}
      
      self.send_request(request)


  def request_rename_file(self,from_name, to_name):
      request = {}
      request["COMMAND"] = "FILE_RENAME"
      request["DATA"] = {"FROM_NAME":from_name, "TO_NAME":to_name.encode()}
      
      self.send_request(request)

  def request_heap_space(self):
         
      request = {}
      request["COMMAND"] = "HEAP_SPACE"
      request["DATA"] = "N/A"
      self.send_request(request)
      
  def request_list_directory(self,mount_point):
         
      request = {}
      request["COMMAND"] = "FILE_DIR"
      request["DATA"] = {"FILE_MOUNT": mount_point}
      self.send_request(request)  


  def send_request(self,msg_dict):
     binary_data = msgpack.packb(msg_dict, use_bin_type=True)
     crc16_bin = self.crc16(binary_data)
     crc_16_str = '{0:x}'.format(crc16_bin)     
     ascii_packet = binascii.hexlify(binary_data)+crc_16_str.encode()+b'\n'
     print("ascii_packet",ascii_packet)
     self.serial_handler.handle.write(ascii_packet)