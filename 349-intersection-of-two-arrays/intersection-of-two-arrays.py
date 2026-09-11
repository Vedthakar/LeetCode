class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p1 = 0
        p2 = 0 
        newarr = []
        nums1.sort()
        nums2.sort()
        while(p1 < len(nums1) and p2 < len(nums2)):
            if(nums1[p1] == nums2[p2] and nums1[p1] not in newarr):
                newarr.append(nums1[p1])
                p1 += 1
                p2 += 1
                continue
            if(nums1[p1] < nums2[p2]):
                p1 += 1
                continue
            else:
                p2+=1
                continue
        return newarr

             