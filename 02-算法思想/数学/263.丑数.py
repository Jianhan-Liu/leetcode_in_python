"""
  @Author       : liujianhan
  @Date         : 2020/6/30 下午7:28
  @Project      : leetcode_in_python
  @FileName     : 263.丑数.py
  @Description  : 编写一个程序判断给定的数是否为丑数。
    丑数就是只包含质因数 2, 3, 5 的正整数。
    示例 1:
    输入: 6
    输出: true
    解释: 6 = 2 × 3
    示例 2:
    输入: 8
    输出: true
    解释: 8 = 2 × 2 × 2
    示例 3:
    输入: 14
    输出: false
    解释: 14 不是丑数，因为它包含了另外一个质因数 7。
    说明：
    1 是丑数。
    输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。
"""


class Solution:
    # 52ms, 13.6MB
    @staticmethod
    def is_ugly(num: int) -> bool:
        for p in 2, 3, 5:
            while num % p == 0 and num > 0:
                num //= p
        return num == 1


if __name__ == '__main__':
    test_cases = [
        6, 8, 14
    ]
    for tc in test_cases:
        print(Solution.is_ugly(tc))
