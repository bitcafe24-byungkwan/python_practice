"""
문제1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요
"""
number = input('수를 입력하세요 : ')
print("3의 배수" + (" 입니다" if not (int(number) % 3) else "가 아닙니다"))
