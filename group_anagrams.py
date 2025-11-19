class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = {}
        for str_ in strs: 
            char_map = {} 
            for s in str_: 
                char_map[s] = char_map.get(s,0) + 1 
            char_tuples = tuple(sorted([(c, count) for c, count in char_map.items()]))
            if char_tuples in result_map:
                result_map[char_tuples].append(str_)
            else:
                result_map[char_tuples] = [str_]
        return list(result_map.values())
    
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        result_map = {}
        final_list = []
        for i in range(0, len(strs)):
            sort_key = "".join(sorted(strs[i])) 
            if sort_key not in result_map:
                result_map[sort_key] = [strs[i]]
            else:
                result_map[sort_key].append(strs[i])
        return list(result_map.values())


# Notes
# Time complexity solution 1: O(n*m), Space complexity solution 1: O(26*k)+O(n)+O(n*m) for output
# Time complexity solution 2: O(n*mlogm), Space complexity solution 2: O(s*k)+O(n)+O(n*m) for output
# the diff is space of the key - in first solution is O(1) cause max can be 26 and in second O(s)
# the diff in time is that sorting the bounded key is O(1) too
