"""
  @Author       : Liujianhan
  @Date         : 20/4/11 23:00
  @FileName     : 887.鸡蛋掉落(H).py
  @ProjectName  : leetcode_in_python
  @Description  : 你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
    每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
    你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
    每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
    你的目标是确切地知道 F 的值是多少。
    无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
    示例 1：

    输入：K = 1, N = 2
    输出：2
    解释：
    鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
    否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
    如果它没碎，那么我们肯定知道 F = 2 。
    因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
    示例 2：

    输入：K = 2, N = 6
    输出：3
    示例 3：

    输入：K = 3, N = 14
    输出：4
     
    提示：

    1 <= K <= 100
    1 <= N <= 10000
 """


class Solution:
    # 1128ms, 23.8MB
    @classmethod
    def super_egg_drop(cls, k: int, n: int) -> int:
        """O(kn*logn), O(kn)"""
        memo = {}

        def dp(k, n):
            if (k, n) not in memo:
                if not n:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    low, high = 1, n
                    while low + 1 < high:
                        temp = (low + high) // 2
                        t1 = dp(k - 1, temp - 1)
                        t2 = dp(k, n - temp)

                        if t1 < t2:
                            low = temp
                        elif t1 > t2:
                            high = temp
                        else:
                            low = high = temp

                    ans = 1 + min(max(dp(k - 1, temp - 1), dp(k, n - temp))
                                  for temp in (low, high))

                memo[k, n] = ans

            return memo[k, n]

        return dp(k, n)

    # out of time
    @classmethod
    def super_egg_drop_v2(cls, k: int, n: int) -> int:
        """O(kn), O(n)"""
        dp = list(range(n + 1))
        dp2 = [0] * (n+1)
        for k in range(2, k+1):
            x = 1
            for n in range(1, n+1):
                while x < n and max(dp[x-1], dp2[n-x]) >= max(dp[x], dp2[n-x-1]):
                    x += 1

                dp2[n] = 1 + max(dp[x-1], dp2[n-x])

            dp = dp2[:]

        return dp[-1]


if __name__ == '__main__':
    test_cases = [(1, 2), (2, 6), (3, 14), (100, 8192)]
    for tc in test_cases:
        print(tc, Solution.super_egg_drop(*tc))
        print(tc, Solution.super_egg_drop_v2(*tc))
