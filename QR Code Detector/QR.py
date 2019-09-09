
# Import modules
import cv2
import matplotlib.pyplot as plt
%matplotlib inline
import matplotlib

matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)

# Read Image
imgPath = "sample_2.jpg"
img = cv2.imread(imgPath)

# Create object
qrDecoder = cv2.QRCodeDetector()

# Detect QR Code
opencvData, bbox, rectifiedImage = qrDecoder.detectAndDecode(img)

# Check if a QR Code has been detected
if opencvData != None:
    print("QR Code Detected")
    print("Decoded Data : {}".format(opencvData))
    # Draw bounding box
    n = len(bbox)
    for i in range(n):
        cv2.line(img, tuple(bbox[i][0]), tuple(bbox[ (i+1) % n][0]), (255,0,0), 2)

    cv2.imwrite("resultImage", img)
    plt.imshow(img[:,:,::-1])
    display(img, bbox)
    rectifiedimg = np.uint8(rectifiedImage);
    cv2.imshow("Rectified QRCode", rectifiedImage);
else:
    print("QR Code NOT Detected")
    cv2.imshow("Results", img)

