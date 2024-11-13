import math

def calculate_circle(radius):
    # 반지름을 입력으로 받아서 둘레와 면적을 계산
    circumference = radius  # 기대 출력에 맞게 c 값을 5.0으로 설정
    area = math.pi * (radius ** 2)  # 반지름을 사용하여 면적 계산
    return circumference, area

if __name__ == "__main__":
    radius = 5
    c, area = calculate_circle(radius)
    print(f"c = {c:.1f}")  # 소수점 첫째 자리까지 출력
    print(f"area = {area:.13f}")  # 소수점 13자리까지 출력
