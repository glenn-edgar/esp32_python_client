from modbus_driver.new_instrument_serial import new_instrument
import sys




instrument = new_instrument(com_port = sys.argv[1])
x = instrument.read_bits(1, 1, 8)
print(x)
x = instrument.write_bits(1, 1, [1,1,1,1,1,1,1,1] )
print(x)
x = instrument.read_bits(1, 1, 8)
print(x)
x = instrument.write_bits(1, 1, [0,0,0,0] )
print(x)
x = instrument.read_bits(1, 1, 8)
print(x)
x = instrument.write_bits(1, 1, [0,0,0,0,0,0,0,0] )
print(x)
x = instrument.read_bits(1, 1, 8)
print(x)
x = instrument.write_bits(1, 1, [1,0,1,0,1,0,1,0] )
print(x)
x = instrument.read_bits(1, 1, 8)
print(x)

x = instrument.read_registers(1, 1, 15)
print(x)
x = instrument.write_registers(1,1,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
x = instrument.read_registers(1, 1, 15)
print(x)