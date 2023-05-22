
"""
aruco.py
---------------

Code to examine if aruco markers can be detected on the recorded sequence
A rectangle will be drawn on markers that are detected

"""

import numpy as np
import cv2
import cv2.aruco as aruco
import glob
import png
import sys

mtx = np.array([[633.09029639, 0., 629.06462963], [0., 638.7544391, 362.74013262],[0., 0., 1.]])
dist = np.array([[-0.04797802,  0.04744357,  0.00017416,  0.00067967, -0.00408397]])

def print_usage():
    
    print("Usage: aruco.py <path>")
    print("path: all or name of the folder")
    print("e.g., aruco.py all, aruco.py.py LINEMOD/Cheezit")
    
    
if __name__ == "__main__":
  
    try:
        if sys.argv[1] == "all":
            folders = glob.glob("LINEMOD/*/")
        elif sys.argv[1]+"/" in glob.glob("LINEMOD/*/"):
            folders = [sys.argv[1]+"/"]
        else:
            print_usage()
            exit()
    except:
        print_usage()
        exit()
       
    rvecs = []
    tvecs = []
    for path in folders:
        print(path)
        for Filename in range(len(glob.glob1(path+"JPEGImages","*.jpg"))):
            img_file = path + 'JPEGImages/%s.jpg' % (Filename)
            color = cv2.imread(img_file)
            gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
            aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
            parameters =  aruco.DetectorParameters_create()
            #detector = aruco.ArucoDetector(aruco_dict, parameters)

            #lists of ids and the corners beloning to each id
            corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters) 
            #detector.detectMarkers(gray)

            font = cv2.FONT_HERSHEY_SIMPLEX 

            if np.all(ids != None):

                aruco.drawDetectedMarkers(color, corners) #Draw A square around the markers
                
                rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[np.where(ids == 1)[0][0]], 0.045, mtx, dist)
                rvecs.append(rvec)
                tvecs.append(tvec)

                ###### DRAW ID #####
                cv2.putText(color, "Id: " + str(ids), (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)


            # Display the resulting frame
            cv2.imshow('Aruco detection on depth thresholded image',color)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            



    cv2.destroyAllWindows()
    
    np.save('tvecs.npy', np.array(tvecs))
    np.save('rvecs.npy', np.array(rvecs))
    
