
# utils.py

import math

def calculate_distance(point1, point2):
    """
    두 점 간의 유클리드 거리를 계산합니다.

    Args:
        point1 (tuple): 첫 번째 점의 좌표 (x1, y1).
        point2 (tuple): 두 번째 점의 좌표 (x2, y2).

    Returns:
        float: 두 점 간의 거리.
    """
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance
