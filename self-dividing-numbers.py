class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def is_self_dividing(number):
            temp = number
            while temp > 0:
                digit = temp % 10
                # If digit is 0 or number is not divisible by digit, return False
                if digit == 0 or number % digit != 0:
                    return False
                temp //= 10
            return True

        # Generate the list of self-dividing numbers
        return [num for num in range(left, right+1) if is_self_dividing(num)]

sol = Solution()
print(sol.selfDividingNumbers(1, 22)) 
print(sol.selfDividingNumbers(47, 85)) 
