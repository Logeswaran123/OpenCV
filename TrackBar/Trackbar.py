import cv2

maxScaleUp = 100
scaleFactor = 1
scaleType = 0
maxType = 1

windowName = "Resize Image"
trackbarValue = "Scale"
trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down"

# load an image
im = cv2.imread("sample_2.jpg")

# Create a window to display results
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

# Callback functions
def scaleImage(*args):
    global scaleFactor
    global scaleType
    
    _type = cv2.getTrackbarPos(trackbarType, windowName)
    
    # Get the scale factor from the trackbar
    if _type == 0:
        scaleFactor = 1 + args[0]/100.0
    else:
        scaleFactor = 1 - args[0]/100.0
    
    # Perform check if scaleFactor is zero
    if scaleFactor == 0:
        scaleFactor = 1
    
    # Resize the image
    scaledImage = cv2.resize(im, None, fx=scaleFactor,\
            fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)




cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, scaleImage)
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType, scaleImage)

cv2.imshow(windowName, im)
c = cv2.waitKey(0)

cv2.destroyAllWindows()