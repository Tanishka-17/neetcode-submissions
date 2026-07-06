class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        answer=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        buckets=[[] for _ in range(len(nums)+1)]
        for entry,frequency in d.items():
            buckets[frequency].append(entry)
        for bucket in range(len(buckets)-1, -1,-1):
            for i in buckets[bucket]:
                answer.append(i)
                if len(answer)==k:
                    return answer




            