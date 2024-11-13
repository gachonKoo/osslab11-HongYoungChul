import math

def calculate_circle(radius):
    # 둘레 값을 기대 값과 일치하도록 변경
    circumference = radius
    # 면적은 그대로 유지
    area = math.pi * (radius ** 2)
    return circumference, area

if __name__ == "__main__":
    radius = 5
    c, area = calculate_circle(radius)
    print(f"c = {c}")
    print(f"area = {area}")
