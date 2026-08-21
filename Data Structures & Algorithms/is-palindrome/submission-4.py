class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(char for char in s if char.isalnum()).lower()
        print(word)
        start = 0
        end = len(word) - 1
        while start <= end:
            if word[start] == word[end]:
                start += 1
                end -= 1
            else:
                return False
        return True