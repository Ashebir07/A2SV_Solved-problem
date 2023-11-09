class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [kelvin, fahrenheit]

sol = Solution()
print(sol.convertTemperature(36.50))   
print(sol.convertTemperature(122.11)) 
