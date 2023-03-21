garo = float(input("가로:"))
saero = float(input("세로:"))
height = float(input("높이:"))

volume = garo * saero * height

print("박스의 부피는")
print(volume,"입니다.")
# 여기까지 박스 부피 구하는 프로그램
total_length = garo + saero + height

if total_length <= 80:
    cost = 5000

elif total_length <= 100:
    cost = 8000
    
elif total_length <= 120:
    cost = 10000

elif total_length <= 160:
    cost = 13000

else:
    cost = "알 수 없음"
    
print("택배비용:", cost)
# 택배비용 계산 프로그램 (2023/03/21 추가)
