import serial
import sys

#A serial port-scanner for linux and windows platforms

def ListAvailablePorts():
    #This function return a list containing the string names for Virtual Serial Ports
    #availables in the computer (this function works only for Windows & Linux Platforms)
    #if there isn't available ports, returns an empty List
    AvailablePorts = []
    platform = sys.platform
    if platform == 'win32':
        for i in range(255):
            try:
                ser = serial.Serial(i,9600)
            except serial.serialutil.SerialException:
                pass
            else:
                AvailablePorts.append(ser.portstr)
                ser.close()
            
    elif platform == 'linux':
        for i in range(0,255):
            try:
                ser = serial.Serial('/dev/ttyUSB'+str(i))
            except serial.serialutil.SerialException:
                pass
            else:
                AvailablePorts.append('/dev/ttyUSB'+str(i))
                ser.close()
    else:
        print '''This method was developed only for linux and windows
                the current platform isn't recognised'''
    return AvailablePorts

        
#print ListAvailablePorts()  #example of how it works
