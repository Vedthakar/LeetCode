class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has = dict(Counter(nums))
        print(has)
        has = dict(sorted(has.items(), key=lambda item: item[1], reverse=True))
        print(has)
        result = []
        for i in has.keys():
            if(k == 0):
                break
            result.append(i)
            k -= 1
        return result