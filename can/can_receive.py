import os
import can

os.system('sudo ip link set can0 type can bitrate 100000')
os.system('sudo ifconfig can0 up')

can0 = can.Bus(channel = 'can0', bustype = 'socketcan')# socketcan_native

msg = can0.recv(10.0)
print(msg)
if msg is None:
    print('Timeout occurred, no message.')

os.system('sudo ifconfig can0 down')