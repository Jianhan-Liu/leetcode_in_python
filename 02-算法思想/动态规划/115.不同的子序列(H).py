"""
  @Author       : Liujianhan
  @Date         : 20/5/8 22:25
  @FileName     : 115.不同的子序列(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
    一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
    题目数据保证答案符合 32 位带符号整数范围。
    示例 1：
    输入：S = "rabbbit", T = "rabbit"
    输出：3
    解释：
    如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
    (上箭头符号 ^ 表示选取的字母)
    rabbbit
    ^^^^ ^^
    rabbbit
    ^^ ^^^^
    rabbbit
    ^^^ ^^^
    示例 2：
    输入：S = "babgbag", T = "bag"
    输出：5
    解释：
    如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。
    (上箭头符号 ^ 表示选取的字母)
    babgbag
    ^^ ^
    babgbag
    ^^    ^
    babgbag
    ^    ^^
    babgbag
      ^  ^^
    babgbag
        ^^^
 """


class Solution:
    # 140ms, 17.5MB
    @classmethod
    def num_distinct(cls, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for j in range(n1 + 1):
            dp[0][j] = 1
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    test_cases = [
        ("rabbbit", "rabbit"),
        ("babgbag", "bag")
    ]
    for tc in test_cases:
        print(Solution.num_distinct(*tc))
