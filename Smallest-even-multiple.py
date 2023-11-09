class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n if n % 2 == 0 else n * 2

sol = Solution()
print(sol.smallestEvenMultiple(5))  
print(sol.smallestEvenMultiple(6)) 
