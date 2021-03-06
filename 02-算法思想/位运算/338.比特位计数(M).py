"""
  @Author       : liujianhan
  @Date         : 2020/9/28 11:56
  @Project      : leetcode_in_python
  @FileName     : 338.比特位计数(M).py
  @Description  : 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

    示例 1:

    输入: 2
    输出: [0,1,1]
    示例 2:

    输入: 5
    输出: [0,1,1,2,1,2]
    进阶:

    给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
    要求算法的空间复杂度为O(n)。
    你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
"""
from typing import List


class Solution:
    # 96ms, 20.2MB
    @staticmethod
    def count_bits(num: int) -> List[int]:
        res = [0] * (num + 1)
        for i in range(0, num + 1):
            res[i] = (i & 1) + res[i >> 1]  # 记得加括号 因为 + 优先级 高于 位运算优先级
        return res

    # 84ms, 20MB
    @staticmethod
    def count_bits_v2(num: int) -> List[int]:
        dp = [0]
        for i in range(1, num + 1):
            # 如果i为偶数
            if i % 2 == 0:
                dp.append(dp[i // 2])
            # 如果i为奇数
            else:
                dp.append(dp[i - 1] + 1)
        return dp


if __name__ == '__main__':
    test_cases = [
        2, 5
    ]
    for tc in test_cases:
        print(Solution.count_bits(tc))
        print(Solution.count_bits_v2(tc))
