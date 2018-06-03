import sys
import serial

x=0
try:
    s = serial.Serial("COM3", 9600)
    s.timeout = 1

except serial.SerialException:
    # -- Error al abrir el puerto serie
    sys.stderr.write("Error al abrir puerto (%s)\n" % str("COM3"))
    sys.exit(1)
while (x==0):
    print(s.read(50))

s.close()

