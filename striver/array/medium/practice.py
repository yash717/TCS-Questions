class Solution:
    def uniquePaths(self, m, n):
        def findPath(i, j, m, n):
            if i == (m-1) and j == (n-1):
                return 1
            if i >= m or j >= n:
                return 0
            else:
                return findPath(i+1, j, m, n)+findPath(i, j+1, m, n)
        return findPath(0, 0, m, n)


if __name__ == '__main__':
    obj = Solution()
    a = obj.uniquePaths(3, 7)
    print("total", a)
