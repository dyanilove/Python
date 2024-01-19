# 문자열 변수 선언
# str_var = "This is my python code."
multi_line = """I'm developer.
I use python. 
Thank you."""

# print(str_var)
# print(multi_line)

# 문자열 더하기
inum1 = 12
inum2 = 34
print(inum1+inum2)

snum1 = "12"
snum2 = "34"
print(snum1 + snum2)
print(snum1 * 3)

# 인덱싱
str_var = "This is my python code."
print(str_var[11])  # p
print(str_var[-1])  # .
print(str_var[-5])  # c

# 슬라이싱
print(str_var[11:17])   # python
print(str_var[11:-6])   # python
print(str_var[:10])     # This is my

#isalpha -> 알파벳으로만 구성되어 있는가
str_var2 = "Thisismypythoncode"
print(str_var.isalpha())    # False(공백,마침표 포함)
print(str_var2.isalpha())   # True

# 함수
print(str_var.upper())      # 다 대문자로 변경
print(str_var.swapcase())   # 대문자는 소문자, 소문자는 대문자로 변경
print(str_var.replace("my", "your"))    # 문자 교체


# Format String
weather ="흐림"
temp = 8.9
# 1. % code (%s, %d, %f)
res = "오늘의 날씨는 %s 입니다. 기온은 %f도 입니다." % (weather,temp)
print(res)

# 2. .format()
res = "[{0} / {1}도] 기온은 {1}도 입니다. 오늘의 날씨는 {0} 입니다.".format(weather,temp)
print(res)

# 3. f""
res = f"오늘의 날씨는 {weather} 입니다. 기온은 {temp}도 입니다."
print(res)


# 사용자로부터 값 입력받기
inp = input("값을 입력해주세요.")
# 입력받은 값에 1더해서 출력
num = int(inp) + 1
print(f"입력받은 값({inp})에 1을 더하면, {num} 입니다.")