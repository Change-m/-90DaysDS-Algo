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
        
    
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid = [[a, b] for a, b in points if a == x or b == y]
        ans = min(valid, key=lambda t: abs(t[0] - x) + abs(t[1] - y), default=None)
        return points.index(ans) if ans else -1    # finding the shortest distance of the coordinates
    
    
    
    def isHappy(self, n: int) -> bool:
        '''while n!=1 and n != 4:
            t = 0
            for i in str(n):
                t += int(i)**2
            n = t
        return '''
        record = set()
        while not n ==1:
            n = sum([int(i)**2 for i in str(n)])
            if n in record:
                return False
            else:
                record.add(n)
        return True # 19 = 1^2 + 9^2 = 82 = 8^2 + 2^2 = ....
    
    
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        '''i=0
        while True:
            if s1 == s2:
                return True
            if s1[i]!=s2[i]:
                s1(i), s2(i) = s2(i), s1(i)
                return True
        return False'''
        c=0
        for i,j in zip(s1,s2):
            if i!=j:
                c+=1
        return s1==s2 or sorted(s1)==sorted(s2) and c==2 # swap the not equal alphabet 
    
    
    def preorder(self, root: 'Node') -> List[int]:
        
        traversal = list()
    
        if root:
            traversal.append(root.val)
            for child in root.children:
                traversal += self.preorder(child)
    
            return traversal # N-arr Traversal Pre order Tree
    
