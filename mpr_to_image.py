import cv2


vid = cv2.VideoCapture('Target_Tracking_Sample_Videos/SampleShip3.mp4')

success, image = vid.read()
count = 1
arr = []

while success:
    cv2.imwrite("video_data/frame_%d.jpg" % count, image)
    arr.append("video_data/frame_%d.jpg" % (count))
    success, image = vid.read()
    print (arr[count - 1])
    count += 1
