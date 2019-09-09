# Snipping an image using mouse


import cv2

# Lists to store the pts
left_top=[]
right_bottom=[]

def drawBox(action, x, y, flags, userdata):
    # Referencing global variables 
    global left_top, circumference, i
    # Action to be taken when left mouse button is pressed
    if action==cv2.EVENT_LBUTTONDOWN:
        left_top = [(x,y)]
    
    # Action to be taken when left mouse button is released
    elif action==cv2.EVENT_LBUTTONUP:
        right_bottom=[(x,y)]
        i = i+1
        # Draw the box and save the cropped image
        cv2.rectangle(source_img, left_top[0], right_bottom[0], (0,255,0),1, cv2.LINE_AA)
        image_crop = source_img[left_top[0][1]: right_bottom[0][1], left_top[0][0]: right_bottom[0][0]]
        cv2.imwrite('image_crop{:03d}.png'.format(i), image_crop)
        cv2.imshow("Window",source_img)


source_img = cv2.imread("sample_2.jpg",1)
# Make a dummy image, will be useful to clear the drawing
dummy = source_img.copy()
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawBox)
k = 0
i = 0
# loop until escape character is pressed
while k!=27 :

    cv2.imshow("Window", source_img)
    cv2.putText(source_img,'Choose top left corner, and drag?' ,(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255,255,255), 2 );

    k = cv2.waitKey(20) & 0xFF
    # Another way of cloning
    if k==99:
        source_img= dummy.copy()


cv2.destroyAllWindows()
