import serial
import time
import logging

# Constants for timing
WAITING_TO_SERIAL_CONNECTION = 2
WAITING_TO_SERIAL_RESPONSE = 0.1

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Handmanager:
    def __init__(self, port_name, baud_rate=9600, timeout=1):
        # Initialize the serial connection
        self.serial_connection = serial.Serial(port_name, baud_rate, timeout=timeout)
        time.sleep(WAITING_TO_SERIAL_CONNECTION)  # Wait for the serial connection to settle
        
    def get_click(self):
        # Send a 'click' command to the device via serial port
        print("Sending click command...")
        self.serial_connection.write(b'click')  # Sending 'click' command as byte string
        time.sleep(WAITING_TO_SERIAL_RESPONSE)  # Wait a bit for the device to respond, if necessary
        response = self.serial_connection.readline()  # Read the response from the device
        return response.decode('utf-8').strip()  # Return the response, decoded as a string
    
    def vibrate(self):
        # Send a 'vibrate' command to the device via serial port
        print("Sending vibrate command...")
        self.serial_connection.write(b'vibrate')  # Sending 'vibrate' command as byte string
        time.sleep(WAITING_TO_SERIAL_RESPONSE)  # Wait a bit for the device to respond, if necessary
        response = self.serial_connection.readline()  # Read the response from the device
        return response.decode('utf-8').strip()  # Return the response, decoded as a string
    
    def close(self):
        # Close the serial connection
        self.serial_connection.close()
        print("Serial connection closed.")
