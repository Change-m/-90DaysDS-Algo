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
        
    '''Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.'''   
    
def searchInsert(self, nums: List[int], target: int) -> int:
        h = len(nums)-1
        l = 0
        if target in nums:
            return nums.index(target)
        else:
            while l <= h:
                mid = (l + h)//2
                if target < nums[mid]:
                    h = mid-1
                else:
                    l = mid+1
            return l

        
def sortedSquares(self, nums: List[int]) -> List[int]:
        temp =[]
        for i in nums:
            temp.append(i**2)
        temp.sort()
        return temp        

    
    
def sortedSquares(self, nums: List[int]) -> List[int]:
        '''temp =[]
        for i in nums:
            temp.append(i**2)
        temp.sort()
        return temp'''
        i = 0
        j = len(nums)-1
        temp = []
        while(i<=j):
            if nums[i]*nums[i] > nums[j]*nums[j]:
                temp.append(nums[i]*nums[i])
                i +=1
            else:
                temp.append(nums[j]*nums[j])
                j-=1
        return temp[::-1]
    

def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #approach 1
        for _ in range(k):
            nums.insert(0, nums.pop())
        #approach 2
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]        
        
        
