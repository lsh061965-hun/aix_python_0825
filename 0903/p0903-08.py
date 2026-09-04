# import os

# print("운영체재 : ",os.name)
# print("현재폴더 : ",os.getcwd())
# print("현재파일리스트 : ",os.listdir())
# # os.mkdir("abc")

# news = open("test.txt","r",encoding="utf-8")
# print(news)
# while True:
#     str = news.readline()  # 한줄씩 읽어옴
#     if str == "": break
#     print(str)

import os

print("운영체제 : ",os.name)
print("현재 폴더 : ",os.getcwd()) #현재폴더
print("폴더안 요소 : ",os.listdir()) #현재폴더안 요소
# os.mkdir("abc")
# os.mkdir("aabbcc")

news = open("c:/down/test.txt","r",encoding="utf-8")
while True:
    str = news.readline()  # 1줄씩 읽어오기
    if str == "": break
    print(str,end="")
news.close()