# paper =  """네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서 
# 2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다. 이번 
# 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서 
# 비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다."""

# print(paper)
# print(len(paper))

str1 = "1,홍길동,100,100,300,100"  # 문자열타입

s = str1.split(",")   # split는 특정문자를 기준으로 분리를 해줌
print(s)
print(s[2])

str2 = "2026-08-28"
s1 = str2.split("-")
print(s1)
print(s1[1])

str3 = "EDMS,307-2E-PS-W-611-W008A,VF5766"
s2 = str3.split(",")
print(s2)
print(len(s2))
print(s2[1])

aa = "     안녕하세요?       "
print(aa)
print(aa.strip())             # strip

aaa2 = "    안녕   하세요    "  # 중간에 있는 공백은 제거되지 않는다.
print(aaa2.strip())

aa3 = "aabbcccdddeefff"       # replace("a","k") a를 k로 치환한다( 문자사이의 공백믄자를 없앨 수 있다.)
aa4 = aa3.replace("a","k")
print(aa3)
print(aa4)
aa5 = aaa2.replace(" ","")
print(aa5)

bb = "abcdefghijklmn"     
print(bb.find("k"))         # find : 검색함수 왼쪽부터 검색시작, 있으면 위치를 반환, 없으면 -1
print(bb.rfind("c"))        # rfind : 오른쪽에서 부터 검색 시작