# importing required libraries 
import cv2 
import time 

# opening video capture stream
vcap = cv2.VideoCapture(0)
if vcap.isOpened() is False :
    print("[Exiting]: Error accessing webcam stream.")
    exit(0)
fps_input_stream = int(vcap.get(5))
print("FPS of webcam hardware/input stream: {}".format(fps_input_stream))
grabbed, frame = vcap.read() # reading single frame for initialization/ hardware warm-up

# processing frames in input stream
num_frames_processed = 0 
start = time.time()
while True :
    grabbed, frame = vcap.read()
    if grabbed is False :
        print('[Exiting] No more frames to read')
        break 

    # adding a delay for simulating time taken for processing a frame 
    delay = 0.03 # delay value in seconds. so, delay=1 is equivalent to 1 second 
    time.sleep(delay) 
    num_frames_processed += 1 

    cv2.imshow('frame' , frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
end = time.time()

# printing time elapsed and fps 
elapsed = end-start
fps = num_frames_processed/elapsed 
print("FPS: {} , Elapsed Time: {} , Frames Processed: {}".format(fps, elapsed, num_frames_processed))

# releasing input stream , closing all windows 
vcap.release()
cv2.destroyAllWindows()
