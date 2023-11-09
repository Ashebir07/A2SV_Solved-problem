class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reversed_num = 0
        original_num = x

        while x > 0:
            digit = x % 10
            reversed_num = (reversed_num * 10) + digit
            x = x // 10

        return original_num == reversed_num


sol = Solution()
print(sol.isPalindrome(121))  
print(sol.isPalindrome(-121)) 
print(sol.isPalindrome(10))   
