class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        # have a reverse dict that goes lettering_dict(sorted):string
        # then we can just go thorugh that reverse dict and return its values

        reverse_dict = {}

        for string in strs:
            string_dict = {}

            for char in string:
                string_dict[char] = string_dict.get(char, 0) + 1

            key = tuple(sorted(string_dict.items()))

            if key not in reverse_dict:
                reverse_dict[key] = []
            
            reverse_dict[key].append(string)
        
        return list(reverse_dict.values())
        
