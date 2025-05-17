import time
import cv2
import numpy as np
import telebot

bot = telebot.TeleBot("7380073491:AAGWGVAsQTNSKgxnfwN_ap-cKZZ0F6h3sYw")
chat_id = 1655740991



cam = cv2.VideoCapture(0)
entpasswd = "."
prev_frame = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
current_frame = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
next_frame = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
moveState = False

def diffImg(f0, f1, f2):
    d1 = cv2.absdiff(f2,f1)
    d2 = cv2.absdiff(f1,f0)
    res = cv2.bitwise_and(d1,d2)
    mat = np.ravel(res)
    nzero = np.count_nonzero(mat)
    return nzero,res



mtext = "."

while True:
    st = open("settings/mode.txt", "r")
    read = st.read()
    ret,frame = cam.read()
    frame = cv2.flip(frame,1)
    _,img = cam.read()
    img = cv2.flip(img,1)
    nzero, result = diffImg(prev_frame, current_frame, next_frame)
    if nzero > 150000:
        #print("Движение есть")
        nzero = 0
        cv2.putText(frame, "Движение", (0, 47), cv2.FONT_HERSHEY_COMPLEX, 4, (0, 0, 255), 5)
        if moveState == False:
            cv2.imwrite("photos/1.png",img)
            print(read)
            if read == "1":
                bot.send_photo(chat_id,open("photos/1.png","rb"))
            moveState = True
    else:
        moveState = False
        #print("Чисто")
        cv2.putText(frame, "Чисто", (0, 47), cv2.FONT_HERSHEY_COMPLEX, 4, (0, 255, 0), 5)
    cv2.imshow("frame",frame)
    prev_frame = current_frame
    current_frame = next_frame
    next_frame = cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyAllWindows()
        break


