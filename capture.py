import sys
import cv2
cam = cv2.VideoCapture(0)
winName = "image"
#cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
s, im = cam.read() # captures image
#cv2.imshow(winName, im) # displays captured image
cv2.imwrite(sys.argv[1]+'.jpg',im) # writes image test.bmp to disk
#cv2.waitKey()
