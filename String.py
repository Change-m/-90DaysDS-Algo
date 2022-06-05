#Missing numbers and letters:-

def missingCharacters(s):
    # Write your code here
    s1 = ""
    p = [False for i in range(26)]
    r = []
    for i in range(10):
        if str(i) not in s:
            s1 += str(i)
    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z'):
            p[ord(s[i]) - ord('a')] == True
    for i in range(26):
        if p[i] == False:
            r += chr(i + ord('a'))
        if r[i] not in s:
            s1 += r[i]
    return s1
  
  
class Multiset:
    
    def __init__(self):
        self.item = []

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.item.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if val in self.item:
            self.item.remove(val)

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        if val in self.item:
            return True
    
    def __len__(self):
        # returns the number of elements in the multiset
        if self.item != None:
            return len(self.item)
        else:
            return 0
