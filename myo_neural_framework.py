'''
    Code to run the Duke eNable myoelectric arm. Bluetooth communication with
    the myoband is based on the work by dzhu and Fernando Cosentino.
    The main edits were to add the custom predictor for the predictions.
'''


from __future__ import print_function
from myo_raw import MyoRaw

if __name__ == '__main__':
    myoband = MyoRaw(None, 25)
    myoband.connect()

    try:
        while True:
            myoband.run(1)
    except KeyboardInterrupt:
        pass

    finally:
        myoband.arduino.port.close()
        myoband.disconnect()
        print("Done")
