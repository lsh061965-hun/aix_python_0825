# 리스트 = 배열
# a = 5
# arr = [1,2,3,4,5]
# print(a)
# print(type(a))
# print(arr)      
# print(type(arr)) 
# print(arr[4]+1)  # 리스트는 0부터 주소가 시작한다.
# print(arr[2])    # 3번째 것을 출력 함.
# print(len(arr))   # 리스트 갯수를 알수 있다.

# 리스트는 []시작
# 리스트는 여러개를 저장
# 리스트는 0부터 주소가 시작
# 리스트를 print하면 모두 출력가능
# 리스트의 특정주소로 그 값을 출력할수 있음
# 리스트 갯수 :len()
# 리스트 안에는 모든 타입을 넣을수 있음
# - 정수,실수,문자열,불,리스트,튜플,딕셔너리

# arr = [1,"안녕",1.2,True,[1,2,3]]
# print(arr[1])
# print(arr[3])
# print(arr[4])
# print(arr[4][1]) # 또는
# a = arr[4]
# print(a[1])

# 1-10사이의 숫자 3개를 입력받아
# 랜덤숫자를 맞추면 당첨, 아니면 꽝
# no1 = int(input("1.숫자입력 : "))
# no2 = int(input("2.숫자입력 : "))
# no3 = int(input("3.숫자입력 : "))
# print("입력숫자 : ",no1,no2,no3)

# nom = [0,0,0]
# num[0] = int(input("1.숫자를 입력하세요 : "))
# num[1] = int(input("2.숫자를 입력하세요 : "))
# num[2] = int(input("3.숫자를 입력하세요 : "))
# print("입력숫자 : ",num)

# a = "사과"
# b = "딸기"
# c = "수박"
# d = "참외"
# e = "복숭아"
# # a,b,c,d,e 중 참외가 있는지 확인하고,
# # 있으면 참외가 있습니다.
# # 참외가 없습니다.
# if a=="참외" or b=="참외" or c=="참외" or d=="참외"\
#    or e=="참외":
#     print("참외가 있습니다.")
# else:
#     print("참외가 없습니다.")

# # 리스트
# fruit = ["사과","수박","참외","수박","복숭아"]
# if "참외" in fruit:     # 비교시 리스트는("검색내용" in 리스트)로 가능하다.
#     print("참외가 있습니다.")
# else:
#     print("없습니다.")


# import random
# r_num = random.randint(1,10)
# # 3개의 숫자 입력 
# arr = []
# # 리스트에 값을 추가할시 append사용
# arr.append(int(input("1. 1-10 숫자입력 : ")))
# arr.append(int(input("2. 1-10 숫자입력 : ")))
# arr.append(int(input("3. 1-10 숫자입력 : ")))
# # 1
# if r_num in arr:
#     print("당첨")
# else:
#     print("꽝")
# print(r_num)
# # 2
# if r_num in arr: print("당첨")
# else: print("꽝")
# # 3
# print("당첨") if r_num in arr else print("꽝")

# fruit = ["사과","수박","참외","수박","복숭아"]
# print(fruit[2]) # 3번째 출력
# print(fruit[1:4]) # 2번 부터 4번 앞까지 출력
# print(fruit[2:]) # 2번부터 마지막까지 출력
# print(fruit[:3]) # 처음부터 3앞에까지
# print(fruit[:])  # 모두출력
# print(fruit[::3]) # 하나건너띄우고 3앞가지 출력

# 슬라이싱으로 표현함 [시작:끝:간격]
# arr = [1,2,3,4,5,6,7,8,9]
# print(arr[::2])  # 하나건너띄우고 출력
# print(arr[1::2]) # 1부터 하나건너가며 출력
# print(arr[:-1])  # "-"부호는 역순으로 출력 함, 마지막 제외
# print(arr[::-1])  # 리스트를 역순으로 정렬

# 문자열도 리스트형태로 저장
# name = "안녕하세요. 반갑습니다."
# print(name)
# print(name[1])
# print(name[4])
# print(name[7:10])
# print(name[::-1])
# print(name[::2])
# if "하" in name:
#     print("있습니다.")
# else:
#     print("없습니다.")

# arr = [            # 2차원 배열
#     [1,2,3]
#     [4,5,6]
#     [7,8,9]
# ]
# arr = [[1,2,3],[4,5,6],[7,8,9]]  # 위의 표현과 같다.
# print([1])
# print([1][1])

# arr = [1,2,3]
# arr1 = [4,5,6]
# arr2 = arr+arr1
# arr3 = arr*3
# aa = [0,0,0,0,0,0,0,0,0,0]
# aa1 = [0]*10
# print(arr+arr1)
# print(arr2)
# print(arr3)
# print(aa)
# print(aa1)

# 리스트추가 : append, insert
# arr = [1,2]
# arr.append(3)     # 마지막에 추가하기
# arr.append(5)
# arr.append(9)
# arr.insert(1,20)  # 사이에 끼워넣기
# print(arr)

# a = [1,2,3]
# b = [4,5,6]
# print(a+b)  # 원본에 영향이 없음
# print(a)
# a.extend(b) # 원본의 값을 바꾼다
# print(a)

# 리스트 삭제 - del, pop
# arr = [1,2,3,4,5]
# print(arr)

# # pop
# arr.pop(2)
# print(arr)

# # del
# del arr[1]
# print(arr)

# # remove - 삭제값을 지정
# arr.remove("안녕")

# # clare - 싹다지움

# # 정렬 - 1. 순차정렬(sort), 역순정렬 sort(reverse=True)
arr = [1,12,8,30,7,5,19]
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)

# 원하는 값 in 리스트, 원하는 값 non 리스트
if 7 in arr:
    print("원하는 수가 있다.")
else:
    print("원하는 수가 없다.")
