
import serial
import time

comm_port = "COM8"
ser = serial.Serial(
                        comm_port,
                        baudrate=115200,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout = None
                       )
                       
                       
while True:
   ser.write(b"ABCDEFGHIJKLMNOPQRSTUVWXYZ")
   time.sleep(1)
   print(ser.readline())