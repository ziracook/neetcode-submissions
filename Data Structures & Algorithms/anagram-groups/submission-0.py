class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map char count to list of anagrams
        res = defaultdict(list) # defaultdict creates a key with default if none exist

        # Add each string as an anagram to a hash map
        for s in strs:
            count = [0] * 26 #a-z

            # Create a hash map for each letter and how many times it occurred 
            for c in s:
                letteridx = ord(c) - ord("a")
                count[letteridx] += 1

            # Char frequency needs to be an immutable type (tuple)
            # Mutable collections can't be used as dict keys directly
            res[tuple(count)].append(s)

        return list(res.values())
        