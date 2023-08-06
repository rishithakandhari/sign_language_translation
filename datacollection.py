
import os
import cv2
cap=cv2.VideoCapture(0)
directory='Image/'
while True:
    _,frame=cap.read()
    count = {
             '1': len(os.listdir(directory+"/Best_of_luck")),
             '2': len(os.listdir(directory+"/Hello")),
             '3': len(os.listdir(directory+"/Love")),
            }

    # cv2.putText(frame, "a : "+str(count['a']), (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "b : "+str(count['b']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "c : "+str(count['c']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "d : "+str(count['d']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'Best_of_luck/'+str(count['1'])+'.png',frame)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'Hello/'+str(count['2'])+'.png',frame)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'Love/'+str(count['3'])+'.png',frame)
    
    

cap.release()
cv2.destroyAllWindows()