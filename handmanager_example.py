import handmanager

# Example usage of the class
try:
    # Initialize the Handmanager with the port name
    #device = Handmanager('/dev/ttyUSB0')
    device = handmanager.Handmanager('COM3')

    # Send a click command and log the response
    click_response = device.get_click()
    if click_response:
        print(f"Click Response: {click_response}")

    # Send a vibrate command and log the response
    for i in range(5):
        print(f"Vibrate {i} port")
        vibrate_response = device.vibrate_with_duration(i)
        if vibrate_response:
            print(f"Vibrate Response: {vibrate_response}")

    # Close the serial connection
    device.close()

except Exception as e:
    print(f"An error occurred: {e}")
