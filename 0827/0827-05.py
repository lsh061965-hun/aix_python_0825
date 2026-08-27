import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print("{:02d}월".format(now.month))
print("{:02d}분".format(now.minute))
print("{:02d}초".format(now.second))

# format
# 123 -> 5자리 빈공백 0으로 채워서 출력하시오.

# print("{:015,d}".format(123456789))
# print("{02d}".format(12))
print(now)
#f_date = now.strftime("%y/%m/%d")
f_date = now.strftime("%y년%m월%d일%H시%M분%S초")
print(f_date)