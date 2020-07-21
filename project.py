#------------------------For Single Img Detector---------

import cv2

detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imp_img = cv2.VideoCapture("elon.jpg")

res, img = imp_img.read()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = detect.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

cv2.imshow("Elon Image",img)
cv2.waitKey(0)
imp_img.release()
cv2.destroyAllWindows()


#------------------------For multiple Img Detector-------------

# import cv2,glob         #glob module that access all file that available in perticular folder
#
# all_images = glob.glob("Detector/*.jpg")
# detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#
# for image in all_images:
#     img = cv2.imread(image)
#     gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     faces = detect.detectMultiScale(gray_img,1.1,5)
#
#
#     for (x,y,w,h) in faces:
#         final_img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#
#     cv2.imshow("Face Detection",final_img)
#     cv2.waitKey(2000)
#     cv2.destroyAllWindows()

#------------------------Smile Detector--------------------------------------

# import cv2
#
# detect = cv2.CascadeClassifier("haarcascade_smile.xml")
# imp_img = cv2.VideoCapture("Detector/yoni.jpg")
#
# res, img = imp_img.read()
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# smiles = detect.detectMultiScale(gray,1.9,10)
#
# for (x,y,w,h) in smiles:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
#
# cv2.imshow("Face Detection",img)
# cv2.waitKey(0)
# imp_img.release()
# cv2.destroyAllWindows()