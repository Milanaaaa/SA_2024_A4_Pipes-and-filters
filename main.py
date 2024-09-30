import cv2
import numpy as np
from argparse import ArgumentParser

from filters import Filters

class StreamPipeline:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter):
        self.filters.append(filter)

    def process(self, frame):
        for filter in self.filters:
            frame = filter(frame)

        return frame

def main():
    argp = ArgumentParser('Funny filters')

    argp.add_argument('-w', '--black-and-white',
                      action='store_true',
                      help='Black and white filter')
    argp.add_argument('-m', '--mirror', 
                      action='store_true',
                      help='Mirror filter')
    argp.add_argument('-r', '--resize',
                      type=float,
                      help='Resize filter')
    argp.add_argument('-b', '--blur', type=int,
                      help='Gaussian blur filter')

    args = argp.parse_args()

    cap = cv2.VideoCapture(0)
    
    pipeline = StreamPipeline()

    if args.black_and_white:
        pipeline.add_filter(Filters.black_and_white)
    
    if args.mirror:
        pipeline.add_filter(Filters.mirror)
    
    if args.resize:
        pipeline.add_filter(lambda f: Filters.resize(f, args.resize))
    
    if args.blur:
        pipeline.add_filter(lambda f: Filters.blur(f, args.blur))
    
    while True:
        ret, frame = cap.read()

        if not ret:
            break
                
        cv2.imshow('Funny filters', pipeline.process(frame))
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
