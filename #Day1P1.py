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
    
    
    
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x0 - x1) * (y1 - y) != (x1 - x) * (y0 - y1):
                return False
        return True  #straight line in the graph
    
    
    
    
    
    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = []
        for num in nums1:
            if num >= max(nums2[nums2.index(num):]):
                n += [-1]
            else:
                for num2 in nums2[nums2.index(num):]:
                    if num2 > num:
                        n += [num2]
                        break
        return n # Next Greater Element
        
    
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
    
    
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)
        ans = 0
        for i in range(length):
            ans += ((i+1)*(length-i)+1)//2 * arr[i]
        return ans #take odd subarray of the list and add all the numbers
    
    
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range (len(arr)+1):
            for j in range(i):
                if len(arr[j:i])%2!=0:
                    ans+=sum(arr[j:i])
        return ans
    
    
    
    
    
    
    
    
