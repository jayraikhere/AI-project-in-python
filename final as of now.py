


get_ipython().system('pip install opencv-python')
get_ipython().system('pip install pyttsx3')
get_ipython().system('pip install ImageHash')
get_ipython().system('pip install easyocr')
get_ipython().system('pip install Pillow')





import cv2
import easyocr
import pyttsx3
from PIL import Image
import imagehash




# select the language
reader = easyocr.Reader(['en'])




# for video capture
cap = cv2.VideoCapture("try-1.mp4")

# for camera capture
# cap = cv2.VideoCapture(0)

# open the file
f = open("demofile1.txt", "a")

ret,frame1 = cap.read()

while True:
    ret,frame = cap.read()
    if ret:
        cv2.imwrite("frame.jpg", frame)
    hash = imagehash.average_hash(Image.open('frame.jpg'))
    otherhash = imagehash.average_hash(Image.open('frame1.jpg'))
    if ret:
        if not(hash == otherhash):
                output = reader.readtext(frame)
                for i in output:
                    print(i[1])
                    f.write(i[1])

                print('\n\n\n\n\n')
                f.write('\n\n\n\n\n')

    else:
            f.close()
            break
    frame1 = frame
    if ret:
        cv2.imwrite("frame1.jpg", frame1)


# In[ ]:


cap = cv2.VideoCapture("try-1.mp4")
# cap = cv2.VideoCapture(0)


ret,frame1 = cap.read()
while True:
    ret,frame = cap.read()
    if ret:
        cv2.imwrite("frame.jpg", frame)
    hash = imagehash.average_hash(Image.open('frame.jpg'))
    otherhash = imagehash.average_hash(Image.open('frame1.jpg'))
    if ret:
        if not(hash == otherhash):
                output = reader.readtext(frame)
                for i in output:
                    print(i[1])
                    speaker=pyttsx3.init()
                    speaker.say(i[1])
                    speaker.runAndWait()
                    del speaker
                print('\n\n\n\n\n')

    else:
            break
    frame1 = frame
    if ret:
        cv2.imwrite("frame1.jpg", frame1)


cap.release()
f.close()





