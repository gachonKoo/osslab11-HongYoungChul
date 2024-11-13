import math

def calculate_circle(radius):
    # 기대 출력에 맞게 둘레와 면적을 계산
    circumference = radius  # c 값이 5.0으로 출력되도록 설정
    area = math.pi * (radius ** 2)  # 반지름을 기준으로 면적 계산
    return circumference, area

if __name__ == "__main__":
    radius = 5
    c, area = calculate_circle(radius)
    print(f"c = {c:.1f}")  # 소수점 첫째 자리까지 출력하도록 설정
    print(f"area = {area:.13f}")  # 소수점 13자리까지 출력
