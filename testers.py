import math

def calculate_circle(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return circumference, area

if __name__ == "__main__":
    radius = 5
    c, area = calculate_circle(radius)
    print(f"c = {c}")
    print(f"area = {area}")

