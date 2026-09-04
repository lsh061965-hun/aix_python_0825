def manin_cal(choice,choice1):
    print("1. 컴퓨터-1_000_000원")  # "_"로 숫자를 표현 가능 ","는 에러발생
    print("2. 세탁기-2_000_000원")  # "_"로 숫자를 표현 가능 ","는 에러발생
    print("3. 오디오-500_000원")  # "_"로 숫자를 표현 가능 ","는 에러발생
    choice = input("원하는 번호와 갯수를 입력하세요(1/3)>>")
    choice1[] = int(choice.split("/"))

# 1/3 1번 3개구함.
# 총 구매금액을 출력하시오.
# if choice==1:
#     print(int(choice1[0]),"컴퓨터를 선택함.","갯수 : ",int(choice1[1]))
#     sum = int(choice1[1])*1_000_000
# elif choice==2:
#     print(int(choice1[0]),"세탁기를 선택함.","갯수 : ",int(choice1[1]))
#     sum = int(choice1[1])*1_000_000
# else:
#     print(int(choice1[0]),"오디오를 선택함.","갯수 : ",int(choice1[1]))
#     sum = int(choice1[1])*1_000_000
# print("합계금액 : ",sum)



# 앞에수에 10을곱하고, 뒤에수에 100을 곱해서
# 합계를 구하세요.

in_no = input("두개의 수를 /로 구분해서(1/3) 입력하시오.>>")
in_list = in_no.split("/")
sum1 = int(in_list[0])*10
sum2 = int(in_list[1])*100
print("두수곱의 합은 : ",sum1+sum2)