import cv2
import os

print("���ڳ�ʼ������ͷ,���Ժ�...")
cap = cv2.VideoCapture(0)
name = input("��ʼ���ɹ���\n����������ƴ����������»س��ɼ���ʼ����")
print("�ɼ�������ʼ")
savedpath = r'./faceImages/' + name
os.makedirs(savedpath)
print("������Ϣ���ļ��д����ɹ�")


i = 1

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('data_read', frame)
    savedname = '/'  + str(i) +  '.jpg'
    k = cv2.waitKey(1) & 0xFF
    cv2.imwrite(savedpath + savedname, frame)
    i += 1
    if i>=601:
        break
    print('%s.jpg successful'%(i))
cap.release()
cv2.destroyAllWindows()