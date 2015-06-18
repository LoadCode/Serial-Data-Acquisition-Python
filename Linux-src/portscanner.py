import serial

def ListAvailablePorts():
    #This function return a list containing the string names for Virtual Serial Ports
    #availables in the computer (this function works only for Linux Platforms)
    #if there isn't available ports, returns an empty List
    AvailablePorts = []
    for i in range(0,255):
        try:
            ser = serial.Serial('/dev/ttyUSB'+str(i))
        except serial.serialutil.SerialException:
            pass
        else:
            AvailablePorts.append('/dev/ttyUSB'+str(i))
            ser.close()
    return AvailablePorts

        
#print ListAvailablePorts()  #example of how it works
