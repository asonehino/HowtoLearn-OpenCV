#조건문
import os
os.system('clear')

num = int(input("정수형 숫자를 입력하세요: "))
if num < 0:
    num = 0
    print("음수라 0으로 설정합니다.")
elif num == 0:
    print("0입니다.")
elif num == 1:
    print("1입니다.")
else:
    print("일단 1 이상 입니다.")