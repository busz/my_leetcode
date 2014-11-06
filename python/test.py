# -*- coding: utf-8 -*-

""" this is a file to test the differnece of the frames form my  new method
"""


import os
import cv2

def showDiff(dir):
    while(1):
        imageList = os.listdir(dir);
        image = cv2.imread(dir+imageList[0])
        preGrey = cv2.cvtColor(image, cv2.cv.CV_RGB2GRAY); 
        #preGrey = preGrey + preGrey - cv2.medianBlur(preGrey, 5) #GaussianBlur(preGrey, (3,3), 3)
        fps = 25
        videoWr = cv2.VideoWriter("K:\QTStab\simpleGaussianBlur.avi", cv2.cv.CV_FOURCC('D', 'I', 'V', '3') , fps, (image.shape[1],image.shape[0]), True)
        for i in range( len(imageList) ):
            image = cv2.imread(dir+str(i)+'.jpg')
            image = cv2.GaussianBlur(image, (5,5), 3)
            videoWr.write(image)
            #print imageName
            #grey = cv2.cvtColor( image , cv2.cv.CV_RGB2GRAY );
            #grey = grey + grey - cv2.medianBlur(grey, 5) #cv2.GaussianBlur(grey, (3,3), 3)
            #diff = grey - preGrey
            #diff = abs(diff)
            #diff = cv2.GaussianBlur(diff, (3,3), 2)
            #preGrey = grey
            cv2.imshow("difference",image);
            cv2.waitKey(23);

        break

def reverse(dir , saveDir):
    imageList = os.listdir(dir);
    num = len(imageList) - 3;
    pos = 0
    for i in range(num):
        img = cv2.imread(dir+str(i)+'.jpg')
        cv2.imwrite(saveDir+str(num - 1-i)+'.jpg', img)
        pos = pos+1
    
def main():
    root = "K:/QTStab/r/"
    
    folder = "simple1"
    folderDir = root + folder+'/';
    saveDir = 'E:/input/3Dfail/'+folder+'/'
    if not os.path.exists(saveDir):
        os.mkdir(saveDir);
    
    showDiff(folderDir)
    #reverse(folderDir , saveDir);

if __name__ == "__main__":
    main()