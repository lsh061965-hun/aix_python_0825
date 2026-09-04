# import random
# def ran_num():
#     if cho == 1:



import random

while True:
    print("1. 구구단 출력프로그램")
    print("2. 1-10까지 숫자마추기 프로그램")
    print("3. 두수를 입력받아 +,-,*,/ 결과값 출력프로그램")
    choice = int(input("번호를 선택하세요.(종료하려면 0 입력)"))
    if choice==0:break
    if choice == 1:
        for i in range(10):
            for j in range(10):
                print(i," X ",j," = ",i*j)
    elif choice==2:
        ran_num = random.randint(1,10)
        in_num = int(input("1-10까지의 수를 입력하시오.>> "))
        if in_num==ran_num:
            print("맞추었습니다.")
            print("랜덤수 :",ran_num,"입력한수 : ",in_num)
        else:
            print("꽝입니다.")
            print("랜덤수 :",ran_num,"입력한수 : ",in_num)
    elif choice==3:
        num1 = int(input("첫번째 수 입력 : "))
        num2 = int(input("두번째 수 입력 : "))
        str1 = input("연산형식 입력(+,-,*,/) : ")
        if str1=="+":
            sum = num1+sum2
            print(num1," + ",num2," = ",sum)
        elif str1=="-":
            sum = num1-num2
            print(num1," - ",num2," = ",sum)
        elif str1=="*":
            sum = num1*num2
            print(num1," * ",num2," = ",sum)
        elif str1=="/":
            sum = num1/num2
            print(num1," / ",num2," = ",sum)
    else:
        print("잘못입력했습니다.")


