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

            
def reverseWords(self, s: str) -> str:
        return " ".join(list(map(lambda x: x[::-1], s.split(' '))))

            
            
def reverseWords(self, s: str) -> str:
        return ' '.join([i[::-1] for i in s.split(' ')])
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
        
        
def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r] < target :
                l+=1
            elif numbers[l]+numbers[r] > target :
                r-=1
            else :
                return [l+1,r+1]
            '''Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].'''

            
            
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
def get_length(head):
    if head is None:
        return 0
    else:
        return 1 + get_length(head.next)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        half = int(get_length(head)/2) + 1
        for i in range(1, half):
            head = head.next
        return head
    '''Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.'''

    
    
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while(fast.next):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
'''Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]'''


def lengthOfLongestSubstring(self, s: str) -> int:
        final,l= 0,[]
        for i in s:
            if i in l:
                final=max(final,len(l))
                del l[0:l.index(i)+1]
                l.append(i) 
            else:
                l.append(i)  
                final=max(final,len(l))
        return final 
    
def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left_p = 0
        longest = 0

        for right_p in range(len(s)):
            while s[right_p] in char_set:
                char_set.remove(s[left_p])
                left_p += 1
            char_set.add(s[right_p])
            longest = max(longest, right_p - left_p + 1)

        return longest
    
def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            st = set()
            for j in range(i, len(s)):
                if s[j] in st:
                    break
                st.add(s[j])
                ans = max(ans, len(st))
 
        return ans
    '''Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''

def checkInclusion(self, s1: str, s2: str) -> bool
    if len(s1) > len(s2):
        return False
    length_of_s1 = len(s1)
    s1_counter = Counter(s1)
    window_counter = Counter()
    for i, c in enumerate(s2):
        window_counter[c] += 1
        if i >= length_of_s1:
            element_from_left = s2[i - length_of_s1]
            if window_counter[element_from_left] == 1:
                del window_counter[element_from_left]
            else:
                window_counter[element_from_left] -= 1
         if window_counter == s1_counter:
              return True
      return False
                


