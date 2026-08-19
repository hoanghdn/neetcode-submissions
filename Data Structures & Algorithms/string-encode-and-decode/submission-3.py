class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            string_length = str(len(string))
            res += string_length + "/" + string
        print(res)
        return res

    

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            print(i)

            # Find /
            while s[j] != "/":
                j += 1

            curr_num = int(s[i:j])

            i = j + 1

            res += [s[i:i+curr_num]]
            i = i + curr_num
            print(i)
        return res

