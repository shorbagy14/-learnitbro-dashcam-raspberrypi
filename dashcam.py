import numpy as np
import cv2
import os
import random
import sys
import getopt
import time

segment = 60
fps = 17
width = 1280
height = 720

def current_milli_time():
    return round(time.time() * 1000)

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 
try:
    opts, args = getopt.getopt(sys.argv[1:], "t:f:w:h:",['time=','framerate=', 'width=', 'height='])
except getopt.GetoptError:
    print('Invalid arguments, use the following flags -t <time> -f <framerate> -w <width> -h <height>')
    sys.exit(2)
for opt, arg in opts:
   if opt == '-help':
      print('camera.py -t <time> -f <framerate> -w <width> -h <height>')
      sys.exit()
   elif opt in ("-t", "--time"):
     segment = int(arg)
   elif opt in ("-f", "--framerate"):
     fps = int(arg)
   elif opt in ("-w", "--width"):
     width = int(arg)
   elif opt in ("-h", "--height"):
     height = int(arg)

print('Segment time: ', segment)
print('Frame rate: ', fps)
print('Width: ', width)
print('Height: ', height)

video_codec = cv2.VideoWriter_fourcc(*'MP4V')
name = 'output'
print(name)
name = os.path.join(os.getcwd(), str(name))
print("ALl logs saved in dir:", name)
if not os.path.exists(name):
    os.mkdir(name)

cap = cv2.VideoCapture(0)
ret = cap.set(3, width)
ret = cap.set(4, height)
cur_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

fname = str(current_milli_time())
video_file_count = 1
video_file = os.path.join(name, fname % video_file_count + ".mp4")
print("Capture video saved location : {}".format(video_file))
# Create a video write before entering the loop
video_writer = cv2.VideoWriter(
    video_file, video_codec, fps, (int(cap.get(3)), int(cap.get(4)))
)
    
frameCount = 0
totalFrameCount = 0
while cap.isOpened():
    ret, frame = cap.read()
    frameCount = frameCount+1
    totalFrameCount = totalFrameCount+1
    if ret == True:
        vt = frameCount*1000/fps
        if vt > segment*1000:
            frameCount = 0
            video_file_count += 1
            video_file = os.path.join(name, fname % video_file_count + ".mp4")
            video_writer = cv2.VideoWriter(
                video_file, video_codec, fps, (int(cap.get(3)), int(cap.get(4)))
            )
            print('Finished recording video: ',video_file)
            
        # Write the frame to the current video writer
        video_writer.write(frame)
        vp = video_file;
        vs = convert(frameCount/fps)
        vf = frameCount
        ct = totalFrameCount*1000/fps
        cf = totalFrameCount
        print("%s;%s;%d;%d;%d;%d" % (vp, vs, vt, vf, ct, cf)) 
        print('Video path: ',vp)
        print('Frames number: ',vf)
        print('Video time: ',vt)
        print('Time stamp: ', vs)
        print('Capture frame number: ',cf)
        print('Capture time: ',ct)
        print()
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
       
cap.release()
cv2.destroyAllWindows()
