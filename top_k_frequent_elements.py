class Solution: # [4,4,4] k = 3
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = [[] for i in range(0,len(nums))] # O(n*m) (m = distinct elements)
        dict_ = {}
        result = []
        for i in range(0,len(nums)): 
            dict_[nums[i]] = dict_.get(nums[i],0) + 1 # O(m)
        for key,v in dict_.items(): # O(m) m = num of distinct elements
            lookup[v-1].append(key)
        for j in range(len(lookup)-1,-1,-1):  # O(n)
            if len(lookup[j])>0: # 
                for l in lookup[j]: 
                    result.append(l)
                    k-=1
                    if k == 0:
                        return(result) #result is k



# Bucket Sort or can be Heap
# prvo izgradi klasican element counter map, i onda pomocu tog izgradi map di su keys: "broj ponajvljanja" a valuesi: koji brojevi imaju tolko ponavljanja
