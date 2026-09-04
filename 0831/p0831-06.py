# 읿력한 숫자 모두 저장
noarr = [10,40,2,9,5]
no = []
ans = []
while True:
    i_no = int(input("숫자입력 : "))
    
    # 1. 입력한 숫자 리스트에 저장
    no.append(i_no)

    # 2. 0을 입력할때 반복문 break
    if i_no==0:break
    

for i in no:
    if i in noarr:
        count = count + 1
        ans.append(i,j)

# 3. 반복문 종료시, 입력된 숫자 모두 출력
print("리스트 : ",noarr)
print("입력숫자 : ",no)
