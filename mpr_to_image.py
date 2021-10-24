import cv2


vid = cv2.VideoCapture('Target_Tracking_Sample_Videos/Sample_Ships_One.mp4')

success, image = vid.read()
count = 1
while success:
    cv2.imwrite("video_data/frame_%d.jpg" % count, image)
    success, image = vid.read()
    print ('Saved image ', count)
    count += 1
