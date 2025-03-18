import serial
import time
import logging

# Constants for timing
WAITING_TO_SERIAL_CONNECTION = 2
WAITING_TO_SERIAL_RESPONSE = 0.1
DEFAULT_VIBRATING_TIME = 1
STOP_VIBRATING = 0
START_VIBRATING = 1

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

            """
            self.serial_connection.write(f"1 1".encode())
            print(f"log: 1 1".encode())
            time.sleep(2)  # Wait for Arduino to initialize
            self.serial_connection.write(f"1 0".encode())
            print(f"log: 1 0".encode())
            time.sleep(2)  # Wait for Arduino to initialize

            self.serial_connection.write(f"1 1".encode())
            print(f"log: 1 1".encode())
            time.sleep(2)  # Wait for Arduino to initialize
            self.serial_connection.write(f"1 0".encode())
            print(f"log: 1 0".encode())
            time.sleep(2)  # Wait for Arduino to initialize
            """

            logger.info(f"Successfully connected to {port_name}.")
        except serial.SerialException as e:
            logger.error(f"Error connecting to serial port {port_name}: {e}")
            #self.serial_connection.close()
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

    def vibrate(self, button_number, state):
        """
        Send a 'vibrate' command to the device to start or stop vibrating a specified button.

        :param button_number: The button number to vibrate (e.g., 1, 2, 3, etc.)
        :param state: The state of vibration (1 to start vibrating, 0 to stop vibrating)
        """
        try:
            # Construct the command to send
            command = f"{button_number} {state}"
            logger.debug(f"Sending vibrate command: {command.strip()}...")

            # Send the command to the serial port
            time.sleep(2)
            self.serial_connection.write(command.encode())
            print(command.encode())
            time.sleep(2)
            time.sleep(WAITING_TO_SERIAL_RESPONSE)  # Wait a bit for the device to respond

            # Read and log the response from the device
            response = self.serial_connection.readline().decode('utf-8').strip()
            logger.info(f"Received response to vibrate command: {response}")

            ##########
            """
            self.serial_connection.write(f"1 1".encode())
            print(f"log2: 1 1".encode())
            time.sleep(2)  # Wait for Arduino to initialize
            self.serial_connection.write(f"1 0".encode())
            print(f"log2: 1 0".encode())
            time.sleep(2)  # Wait for Arduino to initialize
            """
            ##########


            return response
        except Exception as e:
            logger.error(f"Error while sending vibrate command: {e}")
            return None

    def start_vibrate(self, button_number):
        """
        Start vibrating the specified button.

        :param button_number: The button number to start vibrating (e.g., 1, 2, 3, etc.)
        """
        logger.info(f"Starting vibration on button {button_number}...")
        return self.vibrate(button_number, 1)  # Sends the command to start vibrating

    def stop_vibrate(self, button_number):
        """
        Stop vibrating the specified button.

        :param button_number: The button number to stop vibrating (e.g., 1, 2, 3, etc.)
        """
        logger.info(f"Stopping vibration on button {button_number}...")
        return self.vibrate(button_number, 0)  # Sends the command to stop vibrating

    def vibrate_with_duration(self, button_number, duration=DEFAULT_VIBRATING_TIME):
        """
        Start vibrating a specified button and stop after a given duration.

        :param button_number: The button number to vibrate (e.g., 1, 2, 3, etc.)
        :param duration: The duration in seconds for the vibration to last.
        """
        try:
            # Start vibrating the button
            logger.info(f"Starting vibration on button {button_number} for {duration} seconds...")
            self.start_vibrate(button_number)

            # Wait for the specified duration
            time.sleep(duration)

            # Stop vibrating the button after the duration
            self.stop_vibrate(button_number)
            logger.info(f"Stopped vibration on button {button_number}.")
        except Exception as e:
            logger.error(f"Error while vibrating button {button_number} for {duration} seconds: {e}")
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
        #device = Handmanager('/dev/ttyUSB0')
        device = Handmanager('COM3')


        # Send a click command and log the response
        click_response = device.get_click()
        if click_response:
            logger.info(f"Click Response: {click_response}")

        # Send a vibrate command and log the response
        vibrate_response = device.vibrate_with_duration(2)
        if vibrate_response:
            logger.info(f"Vibrate Response: {vibrate_response}")
        for i in range(5):
            print(f"Vibrate {i} port")
            vibrate_response = device.vibrate_with_duration(i)
            if vibrate_response:
                logger.info(f"Vibrate Response: {vibrate_response}")

        # Close the serial connection
        device.close()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
