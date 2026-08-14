from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):

        # Maximum power of 2 we need
        self.LOG = n.bit_length()

        # up[node][j] = 2^j-th ancestor of node
        self.up = [[-1] * self.LOG for _ in range(n)]

        # 2^0 = 1st ancestor
        for node in range(n):
            self.up[node][0] = parent[node]

        # Build binary lifting table
        for j in range(1, self.LOG):
            for node in range(n):

                prev = self.up[node][j - 1]

                if prev != -1:
                    self.up[node][j] = self.up[prev][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:

        bit = 0

        while k > 0:

            # If this bit of k is set,
            # jump 2^bit ancestors
            if k & 1:
                node = self.up[node][bit]

                if node == -1:
                    return -1

            k >>= 1
            bit += 1

        return node