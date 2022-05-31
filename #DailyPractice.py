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

        
        
def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[i:i+k] for i in range(len(s)-k+1)}) == 2 ** k
'''Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.'''
