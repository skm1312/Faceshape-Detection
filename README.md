## Faceshape-Detection

This is an application that takes an image file as input and produces the face shape of the person in the image as output (if a face is found in the image).

## Tools / Libraries

The code base is programmed in python. opencv, numpy and dlib libraries have been used to perform image processing, numerical analsysis and computer vision concepts respectively.
We have used the **shape_predictor_68_face_landmarks.dat** file to plot 68 different files facial landmarks. The source for this file can be found at: http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

## How to run the code?

You need to install dlib, cmake and openCV packages for the code to run on your local system. Download the aforementioned dlib library and place it in the same folder as the python file.
Run the code using -- python filename.py
