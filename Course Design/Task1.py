import cv2
import os

print("正在初始化摄像头,请稍后...")
cap = cv2.VideoCapture(0)
name = input("初始化成功！\n请输入姓名拼音（输入后按下回车采集开始）：")
print("采集即将开始")
savedpath = r'./faceImages/' + name
os.makedirs(savedpath)
print("人脸信息子文件夹创建成功")


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