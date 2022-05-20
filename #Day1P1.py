class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1") # count 1 bits in the 32 bit number

      
    def hammingWeight(self, n: int) -> int:
        count=0
        while n!=0:
            rem=n%2;
            if rem==1:
                count+=1
            n//=2
        return count;
      
      
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        q = 0
        while n != 0:
            a = n%10
            p = p * a
            q = q + a
            n = n//10
        return p - q  # 243 -->  a = 2 * 4 * 3, b = 2 + 4 + 3, a-b   
      

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        for i in range (len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0 # triangle largest perameter in nums array if impossible return 0  
        
        
