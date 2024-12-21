class Solution:
    def groupAnagrams(self, strs):
        hashmap = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
    
            key = tuple(count)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(string)

        return list(hashmap.values())