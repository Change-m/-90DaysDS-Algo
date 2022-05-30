class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            return nums.index(target)
            
    
    
    def firstBadVersion(self, n: int) -> int:
        high = n
        low=1
        
        while(high >= low ):
            mid = (high + low) //2
            if isBadVersion(mid) == True:
                high = mid-1
            else:
                low = mid +1
        return low      
        
    ####Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.#####    
    
