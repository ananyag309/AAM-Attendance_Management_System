import datetime
import time

class FaceRecognition:
    # ... (previous code remains unchanged)

    attendance_count = 0
    max_attendance_count = 3

    def __init__(self):
        self.encode_faces()

    def run_recognition(self):
        # ... (previous code remains unchanged)

        while True:
            # ... (previous code remains unchanged)

            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                # ... (previous code remains unchanged)

                # Capture attendance and add time stamps
                if 'unknown' not in name:
                    self.attendance_count += 1
                    print(f'Attendance {self.attendance_count} recorded at {datetime.datetime.now()}')

                    if self.attendance_count >= self.max_attendance_count:
                        print('Attendance completed!')
                        self.attendance_count = 0  # Reset the attendance count

            # ... (previous code remains unchanged)

            if cv2.waitKey(1) == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    fr = FaceRecognition()
    fr.run_recognition()
