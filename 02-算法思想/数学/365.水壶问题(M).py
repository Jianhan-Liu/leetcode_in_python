"""
  @Author       : liujianhan
  @Date         : 2020/9/4 19:05
  @Project      : leetcode_in_python
  @FileName     : 365.水壶问题(M).py
  @Description  : 有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
    如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
    你允许：
    装满任意一个水壶
    清空任意一个水壶
    从一个水壶向另外一个水壶倒水，直到装满或者倒空
    示例 1: (From the famous "Die Hard" example)

    输入: x = 3, y = 5, z = 4
    输出: True
    示例 2:

    输入: x = 2, y = 6, z = 5
    输出: False
"""
import math


class Solution:
    # 48ms, 13.8MB
    @staticmethod
    def can_measure_water(x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0

    # 5432ms, 166.1MB
    @staticmethod
    def can_measure_water_v2(x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in seen:
                continue
            seen.add((remain_x, remain_y))
            # 把 X 壶灌满。
            stack.append((x, remain_y))
            # 把 Y 壶灌满。
            stack.append((remain_x, y))
            # 把 X 壶倒空。
            stack.append((0, remain_y))
            # 把 Y 壶倒空。
            stack.append((remain_x, 0))
            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
            stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
        return False


if __name__ == '__main__':
    test_cases = [
        (3, 5, 4), (2, 6, 5)
    ]
    for tc in test_cases:
        print(Solution.can_measure_water(*tc))
        print(Solution.can_measure_water_v2(*tc))
