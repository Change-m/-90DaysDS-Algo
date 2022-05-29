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
    
    
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        m=0
        for i in range(len(nums)):
            if nums[i] == 0:
                c=c+1
                m=m+1
                
        while c!=0:
            nums.remove(0)
            c=c-1
            
        while m!=0:
            nums.append('0')
            m=m-1#
    
    
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Sum = 0
        for i in range (0, len(accounts)):
            Sum1 = sum(accounts[i])
            if Sum < Sum1:
                Sum = Sum1
        return Sum
    
    
    def interpret(self, command: str) -> str:
        command=command.replace("()","o")
        command=command.replace("(al)","al")
        return command# replace the string from the another string
    
    
    def findTheDifference(self, s: str, t: str) -> str:
        return list((Counter(t) - Counter(s)).keys())[0]
    
    
    
    def freqAlphabets(self, s: str) -> str:
        letters = ' abcdefghijklmnopqrstuvwxyz'        
        res = ''
        
        for i in range(len(s)):
            if s[i] == '#':
                res = res[:-2]
                res += letters[int(s[i - 2:i])]
            else:
                res += letters[int(s[i])]
        
        return res# convert 1-9 to a-i, 10#-26# to j-z
    
    
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        alien_dict = {}
        for i in range(len(order)):
            alien_dict[order[i]] = i
            
        for i in range(len(words)-1):
            for j in range(i , len(words)-1):
                if words[j] == words[j+1]:
                    continue
                l1 = len(words[j])
                l2 = len(words[j+1])
                index = min(l1 , l2)
                for k in range(index):
                    if alien_dict[words[j][k]] > alien_dict[words[j+1][k]]:
                        return False
                    elif alien_dict[words[j][k]] < alien_dict[words[j+1][k]]:
                        break
                    elif k >= (index-1) and l2 < l1:
                        return False                 
        return True
    
    
    def getDecimalValue(self, head: ListNode) -> int:
        '''temp = 0
        F = head.val
        if F[0] == 1:
                temp += 1
        for i in range(1, len(F)):
            if F[i] == 1:
                temp += ((i-1)*2)
        return temp'''
        if head.val == 1 and head.next == None:
            return int(1)
        else:
            s = ''
            pt = head
            while pt:
                s += str(pt.val)
                pt = pt.next
            b = s[::-1]
            b = b[1:]
            add = 0
            count = 1
            for i in b:
                m = (2**count) * int(i)
                add += m
                count += 1

            last = int(s[len(s)-1])
            add += last
            return add
     
     
     
     def getDecimalValue(self, head: ListNode) -> int:
        a = ''
        while head is not None:
            a += str(head.val)
            head = head.next
        
        return int(a, 2)
        
        
        
     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''a = ''
        while head is not None:
            a += str(head.val)
            head = head.next
        b = ceil(len(a)//2)
        d = a[b:len(a)].split()
        return d'''
        f = s = head
        #When the fast reaches the end, the position of the slow is the middle of the linkedlist
        #because the fast move by two and the slow move by one
        while f and f.next is not None :
            f = f.next.next
            s = s.next
        return s   
        
        
     
     def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
        return dfs(root, 0)
    
    
     def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res=0
        q=[(root,0)]
        
        while q:
            node,l=q.pop(0)
            if (not node.left) and (not node.right) and l:
                res+=node.val
            if node.left:
                q.append((node.left,1))
            if node.right:
                q.append((node.right,0))
        
        return res
     
    
     def sortByBits(self, arr: List[int]) -> List[int]:
        '''s1 = []
        s2 = []
        c = 2
        d = []
        arr.sort()
        if 0 in arr:
            s1.append(0)
        if 1 in arr:
            s1.append(1)
        for i in arr[:len(arr)]:
            if i == c:
                s1.append(i)
                c = c+c
            else:
                s2.append(i)
        d = s1 + s2
        return d'''
        return sorted(arr,key=lambda x: (bin(x).count("1"),x))
      
        
        
        
    class MyQueue:
    def __init__(self):
        self.queue = []        

    def push(self, x: int) -> None:
        self.queue.insert(0, x)

    def pop(self) -> int:
        if self.queue:
            return self.queue.pop()

    def peek(self) -> int:
        if self.queue:
            return self.queue[-1]

    def empty(self) -> bool:
        return self.queue == []
    
    
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s))==''.join(sorted(t))#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    
    
    
    class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType ==1 and self.big >=1:
            self.big -=1
            return True
        if carType ==2 and self.medium>=1:
            self.medium -=1
            return True
        if carType ==3 and self.small >=1:
            self.small-=1
            return True
        return False

'''Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.''' 

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
    
    
    
    class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums[::]

    def sumRange(self, left: int, right: int) -> int:
        return sum(i for i in self.arr[left:right+1])
'''Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3'''

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
    
    
    
    
    
    
    
    
    
    
    
