def divide(self, dividend: int, divisor: int) -> int:
        return min(math.floor(dividend / divisor) if dividend / divisor > 0 else math.ceil(dividend / divisor), 2147483647)
  '''Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.'''
