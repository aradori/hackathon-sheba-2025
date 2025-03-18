import tobii_research as tr
import time

def print_details(tr):
    trackers = tr.find_all_eyetrackers()
    print(trackers)
    print(len(trackers))
    for t in trackers:
        print(t)
    print(trackers[0])
    print(help(trackers[0]))
    print(trackers[0].get_eye_tracking_mode())
    print(trackers[0].retrieve_calibration_data())

def eyetracker_info(eyetracker):
    print("==================")
    print("Address: " + eyetracker.address)
    print("Model: " + eyetracker.model)
    print("Name (It's OK if this is empty): " + eyetracker.device_name)
    print("Serial number: " + eyetracker.serial_number)
    print("==================")

def gaze_data_callback(gaze_data):
    # Print gaze points of left and right eye
    print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
        gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
        gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))
    #print(gaze_data)

def pupil_diameter_callback(gaze_data):
    # Print gaze points of left and right eye
    print("Left pupil diameter: ({left_pupil_diameter}) \t Right pupil diameter: ({right_pupil_diameter})".format(
        left_pupil_diameter=gaze_data['left_pupil_diameter'],
        right_pupil_diameter=gaze_data['right_pupil_diameter']))

def main():
    trackers = tr.find_all_eyetrackers()
    my_eyetracker = trackers[0]

    eyetracker_info(my_eyetracker)

    #my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
    my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, pupil_diameter_callback, as_dictionary=True)
    time.sleep(5)

if __name__ == '__main__':
    main()
