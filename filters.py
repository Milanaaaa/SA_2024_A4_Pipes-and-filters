import cv2

class Filters:
    def black_and_white(frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    def mirror(frame):
        return cv2.flip(frame, 1)

    def resize(frame, scale=0.5):
        return cv2.resize(
            frame, 
            (
                int(frame.shape[1] * scale),
                int(frame.shape[0] * scale)
            )
        )

    def blur(frame, k=9):
        k += int(not k % 2)
        return cv2.GaussianBlur(frame, (k, k), 0, 0)
