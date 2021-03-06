"""
  @Author       : liujianhan
  @Date         : 2020/8/28 10:17
  @Project      : leetcode_in_python
  @FileName     : 658.找到K个最接近的元素(M).py
  @Description  : 给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。
    示例 1:
    输入: [1,2,3,4,5], k=4, x=3
    输出: [1,2,3,4]
    示例 2:
    输入: [1,2,3,4,5], k=4, x=-1
    输出: [1,2,3,4]
    说明:
    k 的值为正数，且总是小于给定排序数组的长度。
    数组不为空，且长度不超过 104
    数组里的每个元素与 x 的绝对值不超过 104
"""
from typing import List


class Solution:
    # 48ms, 14.8MB
    @staticmethod
    def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
        size = len(arr)
        left = 0
        right = size - k

        while left < right:
            mid = (left + right) >> 1
            # 尝试从长度为 k + 1 的连续子区间删除一个元素
            # 从而定位左区间端点的边界值
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], 4, 3),
        ([1, 2, 3, 4, 5], 4, -1),
    ]
    for tc in test_cases:
        print(Solution.find_closest_elements(*tc))
