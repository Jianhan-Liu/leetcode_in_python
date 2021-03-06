"""
  @Author       : liujianhan
  @Date         : 2020/9/17 10:29
  @Project      : leetcode_in_python
  @FileName     : 685.冗余连接II(H).py
  @Description  : 在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。
    每一个节点只有一个父节点，除了根节点没有父节点。
    输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。
    附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
    结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。
    返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
    示例 1:

    输入: [[1,2], [1,3], [2,3]]
    输出: [2,3]
    解释: 给定的有向图如下:
      1
     / \
    v   v
    2-->3
    示例 2:

    输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
    输出: [4,1]
    解释: 给定的有向图如下:
    5 <- 1 -> 2
         ^    |
         |    v
         4 <- 3
    注意:

    二维数组大小的在3到1000范围内。
    二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。
"""
from typing import List


class UnionFind:
    def __init__(self, n):
        self.ancestor = list(range(n))

    def union(self, index1: int, index2: int):
        self.ancestor[self.find(index1)] = self.find(index2)

    def find(self, index: int) -> int:
        if self.ancestor[index] != index:
            self.ancestor[index] = self.find(self.ancestor[index])
        return self.ancestor[index]


class Solution:
    # 116ms, 13.8MB
    @staticmethod
    def find_redundant_directed_connection(edges: List[List[int]]) -> List[int]:
        nodes_count = len(edges)
        uf = UnionFind(nodes_count + 1)
        parent = list(range(nodes_count + 1))
        conflict = -1
        cycle = -1
        for i, (node1, node2) in enumerate(edges):
            if parent[node2] != node2:
                conflict = i
            else:
                parent[node2] = node1
                if uf.find(node1) == uf.find(node2):
                    cycle = i
                else:
                    uf.union(node1, node2)

        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflict_edge = edges[conflict]
            if cycle >= 0:
                return [parent[conflict_edge[1]], conflict_edge[1]]
            else:
                return [conflict_edge[0], conflict_edge[1]]

    # 104ms, 13.7MB
    @staticmethod
    def find_redundant_directed_connection_v2(edges: List[List[int]]) -> List[int]:
        record = list(range(0, len(edges) + 1))

        def getroot(n):
            temp = []
            while (record[n] != n):
                temp.append(n)
                n = record[n]
            for i in temp:
                record[i] = n
            return n

        node = 0
        count = [0] * (len(edges) + 1)
        for edge in edges:
            count[edge[1]] += 1
            if count[edge[1]] == 2:
                node = edge[1]

        for edge in edges:
            l, r = getroot(edge[0]), getroot(edge[1])
            if edge[1] == node:
                continue
            if l == r:
                return edge
            else:
                record[r] = l

        for edge in edges:
            if edge[1] != node:
                continue
            l, r = getroot(edge[0]), getroot(edge[1])
            if l == r:
                return edge
            else:
                record[r] = l


if __name__ == '__main__':
    test_cases = [
        [[1, 2], [1, 3], [2, 3]],
        [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
    ]
    for tc in test_cases:
        print(Solution.find_redundant_directed_connection(tc))
        print(Solution.find_redundant_directed_connection_v2(tc))
