#!/usr/bin/python
import serial
import time

arduino = serial.Serial('COM3', baudrate=9600, timeout=3.0)
cadena = ''

while True:
    var = input("Introduzca  un Comando: ")
    arduino.write(var)
    time.sleep(0.1)
    while arduino.inWaiting() > 0:
        cadena += arduino.readline()
        print
        cadena.rstrip('\n')
        cadena = ''
arduino.close()