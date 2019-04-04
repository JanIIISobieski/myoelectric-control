import time
import serial

class Arduino():
    def __init__(self, port='/dev/ttyACM1', baud_rate=9600):
        self.port = serial.Serial(port, baud_rate)
        self.value_recieved = []
        self.timeout = 5

    def close_port(self):
        self.port.close()

    def send_through_serial(self, value):
        self.port.write(str(value).encode())
        print("Sent value")

    def getFromArduino(self):
        print("Getting response")
        byte_data = self.port.readline()
        ser_data = byte_data.decode('utf-8')
        list_data = ser_data.split()
        strVal = ''.join(list_data)
        self.value_recieved = int(strVal)

    def wait_for_response(self):
        print("Waiting for response")
        t1 = time.time()
        while True:
            self.getFromArduino()
            t2 = time.time()
            if (self.value_recieved == 0):
                print("Recieved value from Arduino")
                break
            if (t2 - t1 > self.timeout):
                print("Timeout in waiting for Arduino. Continuing regardless")
                break
