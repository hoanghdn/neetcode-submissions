class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {} 
        t_hash = {}

        for i in range(len(s)):
            curr_letter = s[i]
            if curr_letter not in s_hash:
                s_hash[curr_letter] = 1
            else:
                s_hash[curr_letter] += 1
        
        for i in range(len(t)):
            curr_letter = t[i]
            if curr_letter not in t_hash:
                t_hash[curr_letter] = 1
            else:
                t_hash[curr_letter] += 1

        print(s_hash)
        print(t_hash)

        return s_hash == t_hash