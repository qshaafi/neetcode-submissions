#  Anagram is using another string that contains same characters, only the order of characters can be different
     #same number/quantity of character but meaning can be different
     #example cat anagram of ate
     #we will be using hasmap Using a Hash Set we can search, add, and remove elements really fast
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       #
        #iterate means repeat
        #making sure both are same length of the string
            if len(s) != len(t):
                return False #if not same length return false

        #counting the characters for both string using hashmap
            countS ={}
            countT ={}

            for i in range(len(s)):
            #s character with i index
            #use get this key same thing on left side so it knows where to start and will return 0
                countS[s[i]] = 1 + countS.get(s[i],0) # 0 is the default value
                countT[t[i]] = 1 + countT.get(t[i],0)
        #iterating the hashmap making sure both counts of the hasmap are same and if not then return false
            for c in countS:
                if countS[c] != countT.get(c,0): # c default index and 0 default value
                    return False
     
            return True # if count matches