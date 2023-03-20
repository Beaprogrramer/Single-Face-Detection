#Detect single faces
# from mtcnn import MTCNN
# import cv2
# detector=MTCNN()
# img = cv2.imread('/home/anushka/Documents/facedetection/MTCNN_Image1.jpeg')
# resized_img=cv2.resize(img,(500,500))
# output=detector.detect_faces(resized_img)
# print(output)
# x,y,width,height=output[0]['box']
# cv2.rectangle(resized_img,pt1=(x,y),pt2=((x+width),(y+height)),color=(0,255,0),thickness=3)
# cv2.imshow('image',resized_img)
# cv2.waitKey(0)
