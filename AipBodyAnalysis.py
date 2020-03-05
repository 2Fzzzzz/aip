# coding=utf-8

from aip import AipBodyAnalysis
import cv2
import os
import base64,requests
import json

# """ 你的 APPID AK SK """
APP_ID = '17245297'
API_KEY = 'rYu3mEhrFnWBUI8ILj9j4c1k'
SECRET_KEY = 'DjTIIk86Kzg60tarp60h2WZkjpTUPQOR'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def deleteByNum():
    """删除temp里的文件"""
    dirpath="D:/Project/aip-python/temp/"
    files = os.listdir(dirpath)  # 列出目录下的文件
    for file in files:
            os.remove(dirpath+file)  # 删除文件
    return

def detecetxiyan(image):
    request_url = "	https://aip.baidubce.com/rpc/2.0/ai_custom/v1/detection/xiyan"
    data = {'image': base64.b64encode(image).decode()}
    access_token = "24.c8d5ea8f4e5680acad06ca9c0589be94.2592000.1585993671.282335-17363741"
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=json.dumps(data))
    content = response.json()
    return content

video_path = "D:/Project/xiyanSusai.mp4"
# image_path="D:/Project/xiyan2.jpg"
cap = cv2.VideoCapture(0)
print(cap.isOpened())
frame_count = 1
num=1
success = True
text=[]
text2=""
filenum=1
location=[]
locationXiYan=[]
count=0
while (success):
    text1=""
    success, frame = cap.read()
    cv2.imshow('frame', frame)  # 显示图像帧
    # print('Read a new frame: ', success)
    params = []
    # params.append(cv.CV_IMWRITE_PXM_BINARY)
    params.append(1)
    if frame_count % 30 == 0:
        filenum += 1
        cv2.imwrite("D:/Project/aip-python/temp/video" + "_%d.jpg" % num, frame, params)

        image_path = ("D:/Project/aip-python/temp/video" + "_%d.jpg" % num)
        # image2 = cv2.imread(imagepath)
        # cv2.imshow("test", image2)

        image = get_file_content(image_path)

        """ 如果有可选参数 """
        options = {}
        options["type"] = "headwear"

        """ 带参数调用人体检测与属性识别 """
        resultOption = client.bodyAttr(image, options)
        resultXiyan=detecetxiyan(image)
        print(resultOption)
        print(resultXiyan)
        print("===============================================")

        if resultOption['person_info'][0]["attributes"]!="":
            for x in resultOption['person_info']:
                text.append(x["attributes"]["headwear"]["name"])
                height = x["location"]["height"]
                width = x["location"]["width"]
                top = x["location"]["top"]
                left = x["location"]["left"]
                loc = [height, width, top, left]
                location.append(loc)
                print(location)

        if resultXiyan["results"]!="":
            for x in resultXiyan["results"]:
                text2="XiYan"
                height = x["location"]["height"]
                width = x["location"]["width"]
                top = x["location"]["top"]
                left = x["location"]["left"]
                loc = [height, width, top, left]
                locationXiYan.append(loc)
                print(locationXiYan)
        for i in text:
            if i=="无帽":
                text1="Unwear Helmet"

        if text1=="Unwear Helmet":
            image2 = cv2.imread(image_path)
            for i in location:
                height=i[0]
                width=i[1]
                top=i[2]
                left=i[3]
                cv2.rectangle(image2, (left, top), (left + width, top + height), (0, 255, 0), 2)
            cv2.putText(image2, text1, (400, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imwrite("D:/Project/aip-python/UnwearHelmet/video" + "_%d.jpg" % num, image2, params)
            cv2.imshow("test2", image2)

        if text2=="XiYan":
            image3 = cv2.imread(image_path)
            for i in location:
                height=i[0]
                width=i[1]
                top=i[2]
                left=i[3]
                cv2.rectangle(image3, (left, top), (left + width, top + height), (0, 255, 0), 2)
            cv2.putText(image3, text2, (400, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imwrite("D:/Project/aip-python/XiYan/video" + "_%d.jpg" % num, image3, params)
            cv2.imshow("test", image3)


        num+=1


    if filenum>20:
        print(filenum)
        deleteByNum()
        print( "Temp files deleted")
        filenum=1

    frame_count = frame_count + 1
    location=[]
    locationXiYan=[]


    if cv2.waitKey(20) & 0xFF == ord('q'):  # 每隔20ms采集一帧，按q键退出采集
        break

cap.release()



# imagepath="D:/Project/34.jpg"
# image = get_file_content(imagepath)
#
# """ 调用人体检测与属性识别 """
# resultAll=client.bodyAttr(image)
#
# """ 如果有可选参数 """
# options = {}
# options["type"] = "gender,smoke,headwear"
#
# """ 带参数调用人体检测与属性识别 """
# resultOption=client.bodyAttr(image, options)

# a=client.bodyAttr(image, options)
# text=a["person_info"][0]["attributes"]["smoke"]["name"]
# height=a["person_info"][0]["location"]["height"]
# width=a["person_info"][0]["location"]["width"]
# top=a["person_info"][0]["location"]["top"]
# left=a["person_info"][0]["location"]["left"]
# if text=="未吸烟":
#     text="Unsmoke"


# print(resultOption)
# print("===============================================")
# print(a["person_info"][0]["attributes"]["smoke"]["name"])
# "'height': 466, 'width': 178, 'top': 58, 'score': 0.9998472929000854, 'left': 309}"
#

# #画矩形和添加文字
# image2 = cv2.imread(imagepath)
# cv2.rectangle(image2, (left, top), (left + width, top + height), (0, 255, 0), 2)
# # cv2.imwrite('2.jpg', image2)
# cv2.putText(image2,text, (409,38), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255), 1, cv2.LINE_AA)
# while(1):
#     cv2.imshow("test",image2)
#     if cv2.waitKey(20) & 0xFF == ord('q'):  # 每隔20ms采集一帧，按q键退出采集
#         break
