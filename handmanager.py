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
        """
        Initialize the Handmanager object with a serial connection.
        
        :param port_name: The name of the serial port (e.g., '/dev/ttyUSB0' or 'COM3')
        :param baud_rate: Baud rate for the serial connection (default is 9600)
        :param timeout: Timeout for the serial connection (default is 1 second)
        """
        try:
            logger.info(f"Initializing connection to {port_name}...")
            self.serial_connection = serial.Serial(port_name, baud_rate, timeout=timeout)
            time.sleep(WAITING_TO_SERIAL_CONNECTION)  # Wait for the serial connection to settle
            logger.info(f"Successfully connected to {port_name}.")
        except serial.SerialException as e:
            logger.error(f"Error connecting to serial port {port_name}: {e}")
            raise

    def get_click(self):
        """
        Send a 'click' command to the device and return the response.
        """
        try:
            logger.debug("Sending 'click' command...")
            self.serial_connection.write(b'click')  # Sending 'click' command as byte string
            time.sleep(WAITING_TO_SERIAL_RESPONSE)  # Wait a bit for the device to respond
            response = self.serial_connection.readline().decode('utf-8').strip()
            logger.info(f"Received response to 'click' command: {response}")
            return response
        except Exception as e:
            logger.error(f"Error while sending 'click' command: {e}")
            return None

    def vibrate(self):
        """
        Send a 'vibrate' command to the device and return the response.
        """
        try:
            logger.debug("Sending 'vibrate' command...")
            self.serial_connection.write(b'vibrate')  # Sending 'vibrate' command as byte string
            time.sleep(WAITING_TO_SERIAL_RESPONSE)  # Wait a bit for the device to respond
            response = self.serial_connection.readline().decode('utf-8').strip()
            logger.info(f"Received response to 'vibrate' command: {response}")
            return response
        except Exception as e:
            logger.error(f"Error while sending 'vibrate' command: {e}")
            return None

    def close(self):
        """
        Close the serial connection.
        """
        try:
            if self.serial_connection.is_open:
                self.serial_connection.close()
                logger.info("Serial connection closed.")
        except Exception as e:
            logger.error(f"Error closing the serial connection: {e}")

# Example usage of the class
if __name__ == "__main__":
    try:
        # Initialize the Handmanager with the port name
        device = Handmanager('/dev/ttyUSB0')

        # Send a click command and log the response
        click_response = device.get_click()
        if click_response:
            logger.info(f"Click Response: {click_response}")

        # Send a vibrate command and log the response
        vibrate_response = device.vibrate()
        if vibrate_response:
            logger.info(f"Vibrate Response: {vibrate_response}")

        # Close the serial connection
        device.close()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
