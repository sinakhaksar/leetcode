class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list) -> int:
        lastest_distance = None
        tar_point = -1
        for i in range(len(points)):
            x2, y2 = points[i]
            if x != x2 and y != y2:
                continue
            
            dis = abs(x - x2) + abs(y - y2)
            if lastest_distance is None or dis < lastest_distance:
                lastest_distance = dis
                tar_point = i

        return tar_point