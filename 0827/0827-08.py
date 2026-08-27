# 1-100까지 랜덤숫자 3객를 리스트에 추가
# 1개의 숫자를 입력받아 
# 있으면 당첨, 없으면 꽌
# 랜덤숫자 리스트 출력
# 입력숫자 출력
import random
num = random.randint(1,15)
num1 = random.randint(1,15)
num2 = random.randint(1,15)
arr = [num, num1, num2]                     # 중복된 숫자가 있을 수 있다.
arr2 = random.sample(range(1,15),3)        # 중복된 숫자가 있을 수 없다.
arr.sort()
arr2.sort()
# arr.append(num)
# arr.append(num1)
# arr.append(num2)
inp = int(input("숫자를 입력하세요>>"))
if inp in arr:
    print("첫번째에 당첨 되었습니다.")
    pass
elif inp in arr2:
    print("두번째에 당첨 되었습니다.")
else:
    print("다음기회에 계속")
print("랜덤숫자 : ",arr)
print("랜덤숫자 : ",arr2)
print("입력한 값",inp)

arr2 = random.sample(range(1,100),3)   # 중복된 숫자가 있을 수 없다.