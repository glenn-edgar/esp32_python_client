
print("--------")
from modbus_driver.new_instrument_serial import new_instrument
import sys
import time


print("made it here")
address= int(sys.argv[2])
instrument = new_instrument(com_port = sys.argv[1])
'''
x = instrument.write_bits(address,0,[1,1,1,1, 1,1,1,1 ,1,1,1,1 ,1,1,1,1] )
time.sleep(1)
x = instrument.read_bits(address, 0, 16)

print(x)

for i in range(0,16):
    instrument.write_bits(address,0,[1,1,1,1, 1,1,1,1 ,1,1,1,1 ,1,1,1,1] )
    instrument.write_bits(address,i,[0])
    print(i,instrument.read_bits(address, 0, 16))
    time.sleep(1)
instrument.write_bits(address,0,[1,1,1,1, 1,1,1,1 ,1,1,1,1 ,1,1,1,1] )
'''
instrument.write_registers(address,0,[100])

instrument.write_registers(address,1,[300])

instrument.write_bits(address,0,[0,0,0,0, 0,0,0,0 ,0,0,0,0 ,0,0,0,0] )
time.sleep(2)
time.sleep(15)
x = instrument.read_registers(address, 0 ,1)
print(x)
x = instrument.read_registers(address, 1 ,1)
print(x)
x = instrument.read_registers(address, 2 ,1)
print(x)
#instrument.write_registers(address,2,[0x3000])
time.sleep(130)
x = instrument.read_registers(address, 0 ,1)
print(x)
x = instrument.read_registers(address, 1 ,1)
print(x)
x = instrument.read_registers(address, 2 ,1)
print(x)
exit()
time.sleep(1)
x = instrument.read_registers(address, 0, 1)
print(x)
time.sleep(1)
x = instrument.write_registers(address,1,[0x5555])
time.sleep(1)
x = instrument.read_registers(address, 1, 1)
time.sleep(1)
print(x)
x = instrument.write_registers(address,2,[0xaaaa])
time.sleep(1)
x = instrument.read_registers(address, 2, 1)
print(x)
time.sleep(1)
x = instrument.write_registers(address,3,[0xaaaa])
time.sleep(1)
x = instrument.read_registers(address, 3, 1)
print(x)