# -*- coding: utf-8 -*-

import xlwt
import serial
import time
import portscanner

def InitDataLogging():
    #This function initializes a session of data acquisition
    #sends the character '1' by the previously opened Serial Port 'ser'
    ser.write('1') #restar the arduino
    time.sleep(1.5) #time required to be ready
    ser.write('1') #starts the data logging


def FinishDataLogging():
    #This function finishes the actual data acquisition
    #sends the '0' character by the serial port object 'ser' previously opened
    ser.write('0')
    ser.close()


def SaveData(DataArray,File_name):
    #This function stores a list (data vector) in a Excel file (95-2003 office version)
    libro = xlwt.Workbook()
    hoja  = libro.add_sheet('Hoja 1')
    for i in range(len(DataArray)):
        row = hoja.row(i)
        row.write(0,DataArray[i])
    libro.save(File_name+'.xls')
    

def DataLogging(totalData,fileName):
    #This function gets a number representing how much
    #values you're going to register.
    data = 0.0
    ser.flushInput() #flushes the input buffer (until there isn't characters to read)
    valsVector = [0]*totalData
    for i in range(totalData):
        data = float(ser.readline())
        print data
        valsVector[i] = data
    SaveData(valsVector,fileName)

AvailablePorts = portscanner.ListAvailablePorts()
ser = serial.Serial(AvailablePorts[0],9600,timeout = 1)
InitDataLogging()
DataLogging(200,'Datos')
print 'terminado'
FinishDataLogging()
