import cv2
import numpy as np
import dlib
import math
# Load the detector
detector = dlib.get_frontal_face_detector()
# Load the predictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# read the image
img = cv2.imread(r"E:\Dev\Face-shape-master\Face Shapes\Round\1.jpeg")
# Convert image into grayscale
img = cv2.resize(img, (389,500))
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# Use detector to find landmarks
faces = detector(gray)

for face in faces:
    x1 = face.left() # left point
    y1 = face.top() # top point
    x2 = face.right() # right point
    y2 = face.bottom() # bottom point
    # Create landmark object
    landmarks = predictor(image=gray, box=face)
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=4)

    leftjaw = (landmarks.part(4).x,landmarks.part(4).y)
    rightjaw = (landmarks.part(12).x,landmarks.part(12).y)
    line1 = np.subtract(rightjaw,leftjaw)
    cv2.line(img, leftjaw,rightjaw,color=(0,255,0), thickness = 4)
    #cv2.circle(img=img, center=(x, y), radius=5, color=(0, 255, 0), thickness=-1)
    #cv2.circle(img=img, center=(x1, y1), radius=5, color=(0, 255, 0), thickness=-1)
    
    chin = (landmarks.part(8).x,landmarks.part(8).y)
    top = (landmarks.part(27).x,landmarks.part(27).y)
    line2 = np.subtract(chin,top)
    cv2.line(img, top,chin,color=(0,255,0), thickness = 4)
    #cv2.circle(img=img, center=(x2, y2), radius=5, color=(0, 255, 0), thickness=-1)
    #cv2.circle(img=img, center=(x3, y3), radius=5, color=(0, 255, 0), thickness=-1)
    
    lefteye = (landmarks.part(1).x,landmarks.part(0).y)
    righteye = (landmarks.part(15).x,landmarks.part(0).y)
    line3 = np.subtract(righteye,lefteye)
    cv2.line(img, righteye,lefteye,color=(0,255,0), thickness = 4)
    #cv2.circle(img=img, center=(x3, y3), radius=5, color=(0, 255, 0), thickness=-1)
    #cv2.circle(img=img, center=(x4, y4), radius=5, color=(0, 255, 0), thickness=-1)

    leftjawup = (landmarks.part(2).x,landmarks.part(2).y)
    rightjawup = (landmarks.part(14).x,landmarks.part(14).y)
    line4 = np.subtract(rightjawup,leftjawup)
    cv2.line(img, rightjawup,leftjawup,color=(0,255,0), thickness = 4)
    
try:
    line5 = np.subtract(leftjawup,top)
    cv2.line(img, top,leftjawup,color=(0,255,0), thickness = 4)
    #print(line5)
    
    line6 = np.subtract(rightjawup,top)
    cv2.line(img, top,rightjawup,color=(0,255,0), thickness = 4)
    #print(line6)
    
    line7 = np.subtract(chin,leftjawup)
    cv2.line(img, chin,leftjawup,color=(0,255,0), thickness = 4)
    #print(line7)
    
    line8 = np.subtract(chin,rightjawup)
    cv2.line(img, chin,rightjawup,color=(0,255,0), thickness = 4)
    #print(line8)
    similarity1 = np.std([line5,line6])
    #print("similarity up diag=",similarity1)

    similarity2 = np.std([line7,line8])
    #print("similarity down diag=",similarity2)

    differ = similarity2-similarity1
    #print(differ)
    #print(line1,line2,line3,line4)
    line9 = np.subtract(line3,line4,line1)
    #print(line9)
    similarity = np.std([line1,line3,line4])
    #print("similarity sq=",similarity)

    length = math.sqrt((landmarks.part(27).x - landmarks.part(8).x)**2 + (landmarks.part(27).y - landmarks.part(8).y)**2)
    #print("Length is:",length)
    # show the image
    roundsim = np.std([line2,line4])
    #print("roundsim",roundsim)
    for i in range(1):
        if (differ<60 and (roundsim>65 and roundsim<87)):
            if ((similarity>40) and (similarity1>74.90)):
                print("The face shape is square")
                break
            else:
                print("The face shape is Diamond")
                break
        if roundsim>87:
            if(similarity1>86): 
                print("The face shape is triangular")
            elif((similarity>94.93) and (similarity<107)):
                print("The face shape is round")
            else:
                print("The face shape is square")
except:
    print("It is not a face, Please upload another image")        

cv2.imshow(winname="Face", mat=img)
# Delay between every fram
cv2.waitKey(delay=0)
# Close all windows
cv2.destroyAllWindows()