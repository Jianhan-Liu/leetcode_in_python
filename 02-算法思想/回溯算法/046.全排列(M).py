"""
  @Author       : Liujianhan
  @Date         : 20/4/25 16:02
  @FileName     : 046.全排列(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
    示例:
    输入: [1,2,3]
    输出:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
     """
from itertools import permutations
from typing import List


class Solution:
    # 36ms, 13.8MB
    @classmethod
    def permute(cls, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))

    # 40ms, 14MB
    @classmethod
    def permute_v2(cls, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()

        return res


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3], [3, 4, 5]
    ]
    for tc in test_cases:
        print(Solution.permute(tc))
        print(Solution.permute_v2(tc))
