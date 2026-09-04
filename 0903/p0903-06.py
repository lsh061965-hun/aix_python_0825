s_arr = [
    {"prd_name":"컴퓨터","price":1000000},
    {"prd_name":"냉장고","price":2000000},
    {"prd_name":"오디오","price":500000},
    {"prd_name":"세탁기","price":1500000}
    ] # 1-0,2-1,3-2

# print("1.컴퓨터")
# print("2.냉장고")
# print("3.오디오")
# print("4.세탁기")

# 가장 긴 가격을 기준으로 포맷팅된 문자열의 최대 길이 계산 (콤마 포함)

max_width = max(len(f"{item['price']:,}") for item in s_arr)
print()
for i,item in enumerate(s_arr):
    name = item["prd_name"]
    price = item["price"]
    print(f"{i+1}.{name:<5} : {price:>{max_width},} 원")
print()

# for i,v in enumerate(s_arr):  # i = 번지수(0)부터 시작, v = 나머 내용을 모두 받아옴
#     print(f"{i+1}. {v['prd_name']} : {v['price']:,} 원")

choice = int(input("원하는 번호입력 : "))

if choice == 1:
    print("컴퓨터")
elif choice == 2:
    print("냉장고")
elif choice == 3:
    print("오디오")
elif choice == 4:
    print("세탁기")