import serial

def ListSerialPorts():
    #This function returns a list with the name of all the serial ports availabes
    #returns an empty list if no ports was found on the system
    ports = []
    for i in range(255):
        try:
            ser = serial.Serial(i,9600)
        except serial.serialutil.SerialException:
            pass
        else:
            ports.append(ser.portstr)
            ser.close()
    return ports

#lista = ListSerialPorts()  #Ejemplo de uso
