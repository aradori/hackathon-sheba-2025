import time
import logging
import serial  # Ensure you have installed the pyserial package

# Constants for timing
WAITING_TO_SERIAL_CONNECTION = 2
WAITING_TO_SERIAL_RESPONSE = 0.1
DEFAULT_VIBRATING_TIME = 1
STOP_VIBRATING = 0
START_VIBRATING = 1

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Handmanager class to manage the vibration and click operations.
class Handmanager:
    """
    A class to manage communication with a device over a serial connection.
    It supports commands to start and stop vibration on specific buttons and to send click commands.
    """

    def __init__(self, port_name, baud_rate=9600, timeout=1):
        """
        Initialize the Handmanager object with a serial connection.
        
        :param port_name: The name of the serial port (e.g., '/dev/ttyUSB0' or 'COM3')
        :param baud_rate: Baud rate for the serial connection (default is 9600)
        :param timeout: Timeout for the serial connection (default is 1 second)
        """
        try:
            logger.info("Initializing connection to %s...", port_name)
            self.serial_connection = serial.Serial(port_name, baud_rate, timeout=timeout)
            time.sleep(WAITING_TO_SERIAL_CONNECTION)  # Wait for the serial connection to settle
            logger.info("Successfully connected to %s.", port_name)
        except serial.SerialException as e:
            logger.err
